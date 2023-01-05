# import libraries
import joblib
import pandas as pd
import streamlit as st


# load the ordinal encoder, one-hot encoder, standard scaler, and model
ordinal_encoder = joblib.load('ordinal_encoder.joblib')
one_hot_encoder = joblib.load('one_hot_encoder.joblib')
scaler = joblib.load('scaler.joblib')
final_model = joblib.load('final_model.joblib')


# load the zip_codes dataset
zip_code_df = pd.read_csv('zip_codes.csv')

# get a list of the zip codes
zip_codes = zip_code_df['Zip Code'].tolist()


st.set_page_config(page_title='Customer Churn', layout='wide', initial_sidebar_state='expanded')


st.title('Telecommunications Customer Churn Prediction')


st.header('Demographic Information')
# select one of the zip code options
zip_code = st.selectbox('Zip Code', zip_codes)
# extract the latitude and longitude values for the selected zip code
latitude, longitude = zip_code_df[zip_code_df['Zip Code'] == zip_code][['Latitude', 'Longitude']].values[0]
# select one of the gender options
gender = st.selectbox('Gender', ['Male', 'Female'])
# enter an age
age = st.number_input('Age', min_value=18)
# fit the age value to an age group
if age <= 29:
    age_group = 'Under 30'
elif age <= 65:
    age_group = '30-65'
else:
    age_group = '65 and above'
# select one of the married options
married = st.selectbox('Married', ['Yes', 'No'])
# select the one of the dependents options
dependents = st.selectbox('Dependents', ['Yes', 'No'])
# display the number_of_dependents input field only if the dependents select box is set to 'Yes'
if dependents == 'Yes':
    number_of_dependents = st.number_input('Number of Dependents', min_value=1)
else:
    number_of_dependents = 0


st.header('Service Information')
st.subheader('Phone Service')
# select the one of the phone_service options
phone_service = st.selectbox('Phone Service', ['Yes', 'No'])
# display the multiple_lines input field only if the phone_service select box is set to 'Yes'
if phone_service == 'Yes':
    multiple_lines = st.selectbox('Multiple Lines', ['Yes', 'No'])
else:
    multiple_lines = 'No'

st.subheader('Internet Service')
# select the one of the internet_service options
internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
# display the internet service related input field only if the internet_service select box is not set to 'No'
if internet_service == 'No':
    online_security = 'No'
    online_backup = 'No'
    streaming_tv = 'No'
    streaming_movies = 'No'
    streaming_music = 'No'
    device_protection_plan = 'No'
    premium_tech_support = 'No'
else:
    online_security = st.selectbox('Online Security', ['Yes', 'No'])
    online_backup = st.selectbox('Online Backup', ['Yes', 'No'])
    streaming_tv = st.selectbox('Streaming TV', ['Yes', 'No'])
    streaming_movies = st.selectbox('Streaming Movies', ['Yes', 'No'])
    streaming_music = st.selectbox('Streaming Music', ['Yes', 'No'])
    device_protection_plan = st.selectbox('Device Protection Plan', ['Yes', 'No'])
    premium_tech_support = st.selectbox('Premium Tech Support', ['Yes', 'No'])

st.subheader('Data Service')
# select one of the unlimited_data options
unlimited_data = st.selectbox('Unlimited Data', ['Yes', 'No'])


st.header('Account Information')
# enter a tenure month
tenure_months = st.number_input('Tenure Months', 0, 120)
# fit the tenure month to a tenure month group
if tenure_months <= 5:
    tenure_group = '< 6 months'
elif tenure_months <= 11:
    tenure_group = '6-11 months'
elif tenure_months <= 23:
    tenure_group = '1 year'
elif tenure_months <= 35:
    tenure_group = '2 years'
elif tenure_months <= 47:
    tenure_group = '3 years'
elif tenure_months <= 59:
    tenure_group = '4 years'
else:
    tenure_group = '5 years and above'

# select one of the contract options
contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
# select one of the paperless_billing options
paperless_billing = st.selectbox('Paperless Billing', ['Yes', 'No'])
# select one of the payment_method options
payment_method = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])


st.subheader('Billing or Payment Information')
# enter the monthly charges
monthly_charges = st.number_input('Monthly Charges:', min_value=0.0)
# enter the total charges
total_charges = st.number_input('Total Charges:', min_value=0.0)
# enter the average monthly long distance charges
avg_monthly_long_distance_charges = st.number_input('Average Monthly Long Distance Charges:', min_value=0.0)
# enter total long distance charges
total_long_distance_charges = st.number_input('Total Long Distances Charges:', min_value=0.0)
# enter the monthly gb download
avg_monthly_gb_download = st.number_input('Average Monthly GB Download:', min_value=0.0)
# enter the total extra charges
total_extra_data_charges = st.number_input('Total Extra Data Charges:', min_value=0.0)
# enter the total revenue
total_revenue = st.number_input('Total Revenue:', min_value=0.0)
# enter the total refunds
total_refunds = st.number_input('Total Refunds:', min_value=0.0)


st.header('Marketing Information')
# select one of the offer options
offer = st.selectbox('Offer', ['Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E', 'None'])


st.header('Customer Behaviour or Activity Information')
# enter the satisfaction score
# satisfaction_score = st.number_input('Satisfaction Score', 1, 5)
satisfaction_score = st.number_input('Satisfaction Score', min_value=1, max_value=5)
# enter the customer lifetime value
cltv = st.number_input('Customer Lifetime Value (CLTV):', min_value=0.0)
# select the one of the referred_a_friend options
referred_a_friend = st.selectbox('Referred a Friend', ['Yes', 'No'])
# display the number_of_referrals input field only if the referred_a_friend select box is set to 'Yes'
if referred_a_friend == 'Yes':
    number_of_referrals = st.number_input('Number of Referrals', min_value=1)
else:
    number_of_referrals = 0


# create an empty data frame
input_df = pd.DataFrame()

# add the user input to the dataframe as a new row
input_df = input_df.append({'latitude': latitude, 'longitude': longitude, 'gender': gender, 'dependents': dependents,
                            'phone service': phone_service, 'multiple lines': multiple_lines,
                            'internet service': internet_service, 'online security': online_security,
                            'online backup': online_backup, 'streaming tv': streaming_tv,
                            'streaming movies': streaming_movies, 'contract': contract,
                            'paperless billing': paperless_billing, 'payment method': payment_method,
                            'monthly charges': monthly_charges, 'total charges': total_charges, 'cltv': cltv,
                            'satisfaction score': satisfaction_score, 'married': married,
                            'number of dependents': number_of_dependents, 'referred a friend': referred_a_friend,
                            'number of referrals': number_of_referrals, 'offer': offer,
                            'avg monthly long distance charges': avg_monthly_long_distance_charges,
                            'avg monthly gb download': avg_monthly_gb_download,
                            'device protection plan': device_protection_plan,
                            'premium tech support': premium_tech_support, 'streaming music': streaming_music,
                            'unlimited data': unlimited_data, 'total refunds': total_refunds,
                            'total extra data charges': total_extra_data_charges,
                            'total long distance charges': total_long_distance_charges, 'total revenue': total_revenue,
                            'age group': age_group, 'tenure group': tenure_group}, ignore_index=True)

nominal_cols = ['gender', 'dependents', 'phone service', 'multiple lines', 'internet service', 'online security', 'online backup', 'streaming tv', 'streaming movies', 'contract', 'paperless billing', 'payment method', 'married', 'referred a friend', 'offer', 'device protection plan', 'premium tech support', 'streaming music', 'unlimited data', 'age group', 'tenure group']
numerical_cols = ['latitude', 'longitude', 'monthly charges', 'total charges', 'cltv', 'number of dependents', 'number of referrals', 'avg monthly long distance charges', 'avg monthly gb download', 'total refunds', 'total extra data charges', 'total long distance charges', 'total revenue']


# reshape the test data to 2D
X_test_2d = input_df['satisfaction score'].astype('object').values.reshape(-1, 1)

# use the encoder to transform the  data
X_test_ordinal_encoded = ordinal_encoder.transform(X_test_2d)
X_test_ordinal_encoded_df = pd.DataFrame(X_test_ordinal_encoded, index=input_df.index, columns=['satisfaction score'])

# use the encoder to transform the data
X_test_nominal_encoded = one_hot_encoder.transform(input_df[nominal_cols])
X_test_nominal_encoded_df = pd.DataFrame(X_test_nominal_encoded, index=input_df.index, columns=one_hot_encoder.get_feature_names_out(nominal_cols))

# use the scaler to scale the data
X_test_scaled = scaler.transform(input_df[numerical_cols])
X_test_scaled_df = pd.DataFrame(X_test_scaled, index=input_df.index, columns=numerical_cols)

# combining the ordinal encoded, one-hot encoded, and scaled data for the test set
X_test_encoded_scaled = pd.concat([X_test_ordinal_encoded_df, X_test_nominal_encoded_df, X_test_scaled_df], axis=1)


if st.button('Predict'):
    # make prediction on the data
    result = final_model.predict(X_test_encoded_scaled)

    if result == 1:
        st.error('The customer will leave the company.')
    else:
        st.success('The customer will remain with the company.')