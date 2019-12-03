import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


def run_regression(filename='datafile.csv'):
    data = pd.read_csv(filename, low_memory=False)

    data.head()
    data['Employee Name'] = data['First Name'] + ' ' + data['Last Name']
    data = data.drop(
        columns=['Has Employees', 'Middle Initial', 'Paid by State or Local Government', 'First Name', 'Last Name'])
    data['Base Annualized Salary'] = data['Base Annualized Salary'].replace({',': ''}, regex=True).astype(float)
    # data['Base Annualized Salary'].head()

    # %matplotlib inline
    # round(data['Base Annualized Salary'].groupby(data['Group']).mean(),2).plot(kind='bar',color='#67c29f')
    # plt.title('Average Salary Across Departments')
    # plt.xlabel('Department Names')
    # plt.ylabel('Average Salary')

    data['Fiscal Year End Date'] = pd.to_datetime(data['Fiscal Year End Date'])
    data['Fiscal Year'] = data['Fiscal Year End Date'].dt.year

    # df_grouped = data.groupby(['Group'])
    # for key, group in df_grouped:
    #     group.groupby('Fiscal Year')['Base Annualized Salary'].mean().plot(label=key, figsize = [15,6], linewidth=3)
    #     plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left')
    #     plt.title('Average Salary Across Years For Each Departments')
    #     plt.xlabel('Fiscal Year')
    #     plt.ylabel('Average Salary')

    df_model = pd.DataFrame(
        data[data['Fiscal Year'] == 2018][['Authority Name', 'Title', 'Group', 'Base Annualized Salary']])
    # df_model.head()

    df_model['Authority Code'] = data['Authority Name'].astype('category')
    df_model['Authority Code'] = df_model['Authority Code'].cat.codes

    df_model['Title Code'] = data['Title'].astype('category')
    df_model['Title Code'] = df_model['Title Code'].cat.codes

    df_model['Group Code'] = data['Group'].astype('category')
    df_model['Group Code'] = df_model['Group Code'].cat.codes

    df_model['Authority Code'] = df_model['Authority Code'].astype('object')
    df_model['Title Code'] = df_model['Title Code'].astype('object')
    df_model['Group Code'] = df_model['Group Code'].astype('object')

    # df_model.head()

    df_model = df_model.dropna()
    df_model = df_model.reset_index(drop=True)

    # sum(df_model.isnull().values.ravel())

    X = df_model.iloc[:, 4:7].values
    y = df_model.iloc[:, 3:4].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    regressor_rf = RandomForestRegressor(n_estimators=30)
    regressor_rf.fit(X_train, np.ravel(y_train, order='C'))

    y_pred_rf = regressor_rf.predict(X_test)

    y_pred_rf = np.array([y_pred_rf])
    y_pred_rf = y_pred_rf.T

    df_results_rf = pd.DataFrame(np.hstack((y_test, y_pred_rf)), columns=['Actual', 'Predicted'])

    # df_results_rf.head(10)
    mean_abs_error = metrics.mean_absolute_error(y_test, y_pred_rf)
    rsquared_score = r2_score(y_test, y_pred_rf)
    return df_results_rf, mean_abs_error, rsquared_score

    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred_rf))
    print('R-Sqaure Value:', r2_score(y_test, y_pred_rf))
