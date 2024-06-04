import graphviz
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import (GridSearchCV, cross_val_score,
                                     learning_curve)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, export_graphviz, plot_tree

# 读取训练集和测试集数据
train_data = pd.read_csv(r'C:\Users\徐浩然\Desktop\MLHW\train.csv')
test_data = pd.read_csv(r'C:\Users\徐浩然\Desktop\MLHW\test.csv')
test=test_data

# 数据预处理
irrelevant_features = ['PassengerId', 'Name', 'Ticket', 'Cabin']
train_data = train_data.drop(irrelevant_features, axis=1)
test_data = test_data.drop(irrelevant_features, axis=1)

train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)

test_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)

label_encoder_sex = LabelEncoder()
label_encoder_embarked = LabelEncoder()

train_data['Sex'] = label_encoder_sex.fit_transform(train_data['Sex'])
train_data['Embarked'] = label_encoder_embarked.fit_transform(train_data['Embarked'])

test_data['Sex'] = label_encoder_sex.transform(test_data['Sex'])
test_data['Embarked'] = label_encoder_embarked.transform(test_data['Embarked'])

scaler = MinMaxScaler()
train_data[['Age', 'Fare']] = scaler.fit_transform(train_data[['Age', 'Fare']])
test_data[['Age', 'Fare']] = scaler.transform(test_data[['Age', 'Fare']])






_, ax = plt.subplots(figsize=(10, 10))
corr = train_data.corr(method='pearson')
cmap = sns.diverging_palette(220, 10, as_cmap=True)
_ = sns.heatmap(
    corr,
    cmap=cmap,
    square=True,
    cbar_kws={'shrink': 0.8},
    ax=ax,
    annot=True,
    annot_kws={'fontsize': 12})
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/cor.png',dpi=300)
plt.show()



# 特征和标签
X = train_data.drop('Survived', axis=1)
y = train_data['Survived']



survived_count = train_data['Survived'].value_counts()
positive_samples = survived_count[1]  # 存活的样本数量
negative_samples = survived_count[0]  # 未存活的样本数量
# 饼图
labels = ['Survived (1)', 'Not Survived (0)']
sizes = [positive_samples, negative_samples]
# colors = ['firebrick', 'darkblue']
explode = (0.1, 0)  # 突出显示Survived

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # 保持饼图为圆形
plt.title('Survival Prediction Distribution')
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/s_train.png',dpi=300)
plt.show()




# 1. 随机森林
rf_model = RandomForestClassifier(random_state=42)

# 定义参数网格
rf_param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# 使用 GridSearchCV 进行交叉验证和参数搜索
rf_grid_search = GridSearchCV(estimator=rf_model, param_grid=rf_param_grid, cv=10, scoring='accuracy')
rf_grid_search.fit(X, y)

# 输出最优参数
print("随机森林最优参数:", rf_grid_search.best_params_)

# 交叉验证评估模型性能
rf_cv_scores = cross_val_score(rf_grid_search.best_estimator_, X, y, cv=10, scoring='accuracy')
print("随机森林交叉验证准确率:", rf_cv_scores.mean())


# 随机森林特征重要性可视化
plt.figure(figsize=(10, 6))
importance = pd.Series(rf_grid_search.best_estimator_.feature_importances_, index=X.columns)
importance = importance.sort_values(ascending=False)
sns.barplot(x=importance, y=importance.index, palette='viridis')
plt.title('Random Forest Feature Importance')
plt.xlabel('Feature Importance')
plt.ylabel('Feature')
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/RF_imp.png',dpi=300)
plt.show()











# 2. 支持向量机
svm_model = SVC(random_state=42)

# 定义参数网格
svm_param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf'],
    'gamma': ['scale', 'auto']
}

# 使用 GridSearchCV 进行交叉验证和参数搜索
svm_grid_search = GridSearchCV(estimator=svm_model, param_grid=svm_param_grid, cv=10, scoring='accuracy')
svm_grid_search.fit(X, y)

# 输出最优参数
print("支持向量机最优参数:", svm_grid_search.best_params_)

# 交叉验证评估模型性能
svm_cv_scores = cross_val_score(svm_grid_search.best_estimator_, X, y, cv=10, scoring='accuracy')
print("支持向量机交叉验证准确率:", svm_cv_scores.mean())













# 3. K最近邻
knn_model = KNeighborsClassifier()

# 定义参数网格
knn_param_grid = {
    'n_neighbors': [3, 5, 7],
    'weights': ['uniform', 'distance'],
    'p': [1, 2]
}

# 使用 GridSearchCV 进行交叉验证和参数搜索
knn_grid_search = GridSearchCV(estimator=knn_model, param_grid=knn_param_grid, cv=10, scoring='accuracy')
knn_grid_search.fit(X, y)

# 输出最优参数
print("K最近邻最优参数:", knn_grid_search.best_params_)

# 交叉验证评估模型性能
knn_cv_scores = cross_val_score(knn_grid_search.best_estimator_, X, y, cv=10, scoring='accuracy')
print("K最近邻交叉验证准确率:", knn_cv_scores.mean())














# 4. 决策树
dt_model = DecisionTreeClassifier(random_state=42)

# 定义参数网格
dt_param_grid = {
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# 使用 GridSearchCV 进行交叉验证和参数搜索
dt_grid_search = GridSearchCV(estimator=dt_model, param_grid=dt_param_grid, cv=10, scoring='accuracy')
dt_grid_search.fit(X, y)

# 输出最优参数
print("决策树最优参数:", dt_grid_search.best_params_)

# 交叉验证评估模型性能
dt_cv_scores = cross_val_score(dt_grid_search.best_estimator_, X, y, cv=10, scoring='accuracy')
print("决策树交叉验证准确率:", dt_cv_scores.mean())

# 可视化决策树
plt.figure(figsize=(12, 8))
plot_tree(dt_grid_search.best_estimator_, filled=True, feature_names=X.columns, class_names=['Not Survived', 'Survived'])
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/dtmap.png',dpi=300)
plt.show()



# 特征重要性可视化
feature_importance = pd.Series(dt_grid_search.best_estimator_.feature_importances_, index=X.columns)
feature_importance = feature_importance.sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importance, y=feature_importance.index, palette='viridis')
plt.title('Decision Tree Feature Importance')
plt.xlabel('Feature Importance')
plt.ylabel('Features')
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/dt_imp.png',dpi=300)
plt.show()




# 在测试集上进行预测
rf_predictions = rf_grid_search.best_estimator_.predict(test_data).tolist()
svm_predictions = svm_grid_search.best_estimator_.predict(test_data).tolist()
knn_predictions = knn_grid_search.best_estimator_.predict(test_data).tolist()
dt_predictions = dt_grid_search.best_estimator_.predict(test_data).tolist()




# 预测可视化
# 统计预测结果中0和1的数量
count_0 = rf_predictions.count(0)
count_1 = rf_predictions.count(1)

# 饼图
labels = ['Survived (1)', 'Not Survived (0)']
sizes = [count_1, count_0]
explode = (0.1, 0)  # 突出显示Survived
plt.pie(sizes, explode=explode, labels=labels,  autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # 保持饼图为圆形
plt.title('Survival Prediction Distribution (RF)')
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/s_rf.png',dpi=300)
plt.show()



count_0 = svm_predictions.count(0)
count_1 = svm_predictions.count(1)

# 饼图
labels = ['Survived (1)', 'Not Survived (0)']
sizes = [count_1, count_0]
explode = (0.1, 0)  # 突出显示Survived
plt.pie(sizes, explode=explode, labels=labels,  autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # 保持饼图为圆形
plt.title('Survival Prediction Distribution (SVM)')
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/s_svm.png',dpi=300)
plt.show()


count_0 = knn_predictions.count(0)
count_1 = knn_predictions.count(1)

# 饼图
labels = ['Survived (1)', 'Not Survived (0)']
sizes = [count_1, count_0]
explode = (0.1, 0)  # 突出显示Survived
plt.pie(sizes, explode=explode, labels=labels,  autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # 保持饼图为圆形
plt.title('Survival Prediction Distribution (KNN)')
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/s_knn.png',dpi=300)
plt.show()


count_0 = dt_predictions.count(0)
count_1 = dt_predictions.count(1)

# 饼图
labels = ['Survived (1)', 'Not Survived (0)']
sizes = [count_1, count_0]
explode = (0.1, 0)  # 突出显示Survived
plt.pie(sizes, explode=explode, labels=labels,  autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # 保持饼图为圆形
plt.title('Survival Prediction Distribution (DT)')
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/s_dt.png',dpi=300)
plt.show()




















# 输出模型在测试集上的性能
# 请注意，由于测试集没有真实的标签，无法计算准确率和分类报告
# 通常需要将预测结果提交到实际应用中进行评估
print("\n随机森林在测试集上的预测:", rf_predictions)
print("支持向量机在测试集上的预测:", svm_predictions)
print("K最近邻在测试集上的预测:", knn_predictions)
print("决策树在测试集上的预测:", dt_predictions)


# 随机森林交叉验证准确率可视化
plt.figure(figsize=(8, 5))
sns.barplot(x=['CV1', 'CV2', 'CV3', 'CV4', 'CV5','CV6', 'CV7', 'CV8', 'CV9', 'CV10'], y=rf_cv_scores, color='steelblue')
plt.title('Random Forest Cross-Validation Accuracy')
plt.xlabel('Fold')
plt.ylabel('Accuracy')
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/RF_k.png',dpi=300)
plt.show()

# 支持向量机交叉验证准确率可视化
plt.figure(figsize=(8, 5))
sns.barplot(x=['CV1', 'CV2', 'CV3', 'CV4', 'CV5','CV6', 'CV7', 'CV8', 'CV9', 'CV10'], y=svm_cv_scores, color='orange')
plt.title('Support Vector Machine Cross-Validation Accuracy')
plt.xlabel('Fold')
plt.ylabel('Accuracy')
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/SVM_k.png',dpi=300)
plt.show()

# K最近邻交叉验证准确率可视化
plt.figure(figsize=(8, 5))
sns.barplot(x=['CV1', 'CV2', 'CV3', 'CV4', 'CV5','CV6', 'CV7', 'CV8', 'CV9', 'CV10'], y=knn_cv_scores, color='green')
plt.title('K-Nearest Neighbors Cross-Validation Accuracy')
plt.xlabel('Fold')
plt.ylabel('Accuracy')
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/Knn_k.png',dpi=300)
plt.show()

# 决策树交叉验证准确率可视化
plt.figure(figsize=(8, 5))
sns.barplot(x=['CV1', 'CV2', 'CV3', 'CV4', 'CV5','CV6', 'CV7', 'CV8', 'CV9', 'CV10'], y=dt_cv_scores, color='brown')
plt.title('Decision Tree Cross-Validation Accuracy')
plt.xlabel('Fold')
plt.ylabel('Accuracy')
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/dt_k.png',dpi=300)
plt.show()






# 学习曲线函数
def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None, n_jobs=-1, train_sizes=np.linspace(.1, 1.0, 50)):
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean,  color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean,  color="g",
             label="Cross-validation score")

    plt.legend(loc="best")
    return plt

# 使用学习曲线函数
plot_learning_curve(rf_grid_search.best_estimator_, "Learning Curve (Random Forest)", X, y, cv=10, n_jobs=-1)
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/RF_lc.png',dpi=300)
plt.show()

plot_learning_curve(svm_grid_search.best_estimator_, "Learning Curve (Support Vector Machine)", X, y, cv=10, n_jobs=-1)
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/svm_lc.png',dpi=300)
plt.show()

plot_learning_curve(knn_grid_search.best_estimator_, "Learning Curve (K-Nearest Neighbors)", X, y, cv=10, n_jobs=-1)
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/knn_lc.png',dpi=300)
plt.show()

plot_learning_curve(dt_grid_search.best_estimator_, "Learning Curve (Decision Tree)", X, y, cv=10, n_jobs=-1)
plt.savefig(r'C:/Users/徐浩然/Desktop/MLHW/dt_lc.png',dpi=300)
plt.show()




