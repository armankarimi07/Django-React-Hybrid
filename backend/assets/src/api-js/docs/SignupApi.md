# DjangoFrontendIntegrations.SignupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**signupCreate**](SignupApi.md#signupCreate) | **POST** /api/signup/ | 
[**signupRetrieve**](SignupApi.md#signupRetrieve) | **GET** /api/signup/ | 



## signupCreate

> Signup signupCreate(signup)



### Example

```javascript
import DjangoFrontendIntegrations from 'django_frontend_integrations';
let defaultClient = DjangoFrontendIntegrations.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new DjangoFrontendIntegrations.SignupApi();
let signup = new DjangoFrontendIntegrations.Signup(); // Signup | 
apiInstance.signupCreate(signup, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signup** | [**Signup**](Signup.md)|  | 

### Return type

[**Signup**](Signup.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json


## signupRetrieve

> Signup signupRetrieve()



### Example

```javascript
import DjangoFrontendIntegrations from 'django_frontend_integrations';
let defaultClient = DjangoFrontendIntegrations.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new DjangoFrontendIntegrations.SignupApi();
apiInstance.signupRetrieve((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Signup**](Signup.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

