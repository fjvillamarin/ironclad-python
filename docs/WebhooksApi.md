# openapi_client.WebhooksApi

All URIs are relative to *https://ironcladapp.com/public/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_webhook**](WebhooksApi.md#create_a_webhook) | **POST** /webhooks | Create a Webhook
[**delete_a_webhook**](WebhooksApi.md#delete_a_webhook) | **DELETE** /webhooks/{id} | Delete a Webhook
[**list_all_webhooks**](WebhooksApi.md#list_all_webhooks) | **GET** /webhooks | List All Webhooks
[**retrieve_a_webhook**](WebhooksApi.md#retrieve_a_webhook) | **GET** /webhooks/{id} | Retrieve a Webhook
[**retrieve_webhook_verification_key**](WebhooksApi.md#retrieve_webhook_verification_key) | **GET** /webhooks/verification-key | Retrieve Webhook Verification Key
[**update_a_webhook**](WebhooksApi.md#update_a_webhook) | **PATCH** /webhooks/{id} | Update a Webhook


# **create_a_webhook**
> CreateAWebhook200Response create_a_webhook(create_a_webhook_request=create_a_webhook_request)

Create a Webhook

Creates a webhook for the specified events. Send separate requests if you need to create webhooks for multiple target URLs. Each target URL may only have one active registration.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.create_a_webhook200_response import CreateAWebhook200Response
from openapi_client.models.create_a_webhook_request import CreateAWebhookRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ironcladapp.com/public/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://ironcladapp.com/public/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)
    create_a_webhook_request = openapi_client.CreateAWebhookRequest() # CreateAWebhookRequest |  (optional)

    try:
        # Create a Webhook
        api_response = api_instance.create_a_webhook(create_a_webhook_request=create_a_webhook_request)
        print("The response of WebhooksApi->create_a_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->create_a_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_a_webhook_request** | [**CreateAWebhookRequest**](CreateAWebhookRequest.md)|  | [optional] 

### Return type

[**CreateAWebhook200Response**](CreateAWebhook200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |
**400** | Bad request error when creating webhook. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_webhook**
> object delete_a_webhook(id)

Delete a Webhook

Delete a specific webhook

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ironcladapp.com/public/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://ironcladapp.com/public/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)
    id = 'id_example' # str | The ID of the webhook.

    try:
        # Delete a Webhook
        api_response = api_instance.delete_a_webhook(id)
        print("The response of WebhooksApi->delete_a_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_a_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the webhook. | 

### Return type

**object**

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |
**400** | 400 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_webhooks**
> ListAllWebhooks200Response list_all_webhooks(page=page, page_size=page_size)

List All Webhooks

View all webhooks associated with a specific company with filtering available via query parameters

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.list_all_webhooks200_response import ListAllWebhooks200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ironcladapp.com/public/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://ironcladapp.com/public/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)
    page = 0 # int | The page number used when paginating through a list of results. (optional) (default to 0)
    page_size = 20 # int | A limit of the number of results to return. (optional) (default to 20)

    try:
        # List All Webhooks
        api_response = api_instance.list_all_webhooks(page=page, page_size=page_size)
        print("The response of WebhooksApi->list_all_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->list_all_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number used when paginating through a list of results. | [optional] [default to 0]
 **page_size** | **int**| A limit of the number of results to return. | [optional] [default to 20]

### Return type

[**ListAllWebhooks200Response**](ListAllWebhooks200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |
**400** | 400 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_a_webhook**
> CreateAWebhook200Response retrieve_a_webhook(id)

Retrieve a Webhook

View the data associated with a specific webhook

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.create_a_webhook200_response import CreateAWebhook200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ironcladapp.com/public/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://ironcladapp.com/public/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)
    id = 'id_example' # str | The ID of the webhook.

    try:
        # Retrieve a Webhook
        api_response = api_instance.retrieve_a_webhook(id)
        print("The response of WebhooksApi->retrieve_a_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->retrieve_a_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the webhook. | 

### Return type

[**CreateAWebhook200Response**](CreateAWebhook200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |
**400** | 400 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_webhook_verification_key**
> retrieve_webhook_verification_key()

Retrieve Webhook Verification Key

View the verification key for webhook security implementations

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ironcladapp.com/public/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://ironcladapp.com/public/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)

    try:
        # Retrieve Webhook Verification Key
        api_instance.retrieve_webhook_verification_key()
    except Exception as e:
        print("Exception when calling WebhooksApi->retrieve_webhook_verification_key: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |
**400** | 400 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_webhook**
> CreateAWebhook200Response update_a_webhook(id, update_a_webhook_request=update_a_webhook_request)

Update a Webhook

Update the data associated with a specific webhook

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.create_a_webhook200_response import CreateAWebhook200Response
from openapi_client.models.update_a_webhook_request import UpdateAWebhookRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ironcladapp.com/public/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://ironcladapp.com/public/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhooksApi(api_client)
    id = 'id_example' # str | The ID of the webhook.
    update_a_webhook_request = openapi_client.UpdateAWebhookRequest() # UpdateAWebhookRequest |  (optional)

    try:
        # Update a Webhook
        api_response = api_instance.update_a_webhook(id, update_a_webhook_request=update_a_webhook_request)
        print("The response of WebhooksApi->update_a_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->update_a_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the webhook. | 
 **update_a_webhook_request** | [**UpdateAWebhookRequest**](UpdateAWebhookRequest.md)|  | [optional] 

### Return type

[**CreateAWebhook200Response**](CreateAWebhook200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |
**400** | 400 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

