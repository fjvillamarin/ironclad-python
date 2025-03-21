# openapi_client.RecordsApi

All URIs are relative to *https://ironcladapp.com/public/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_record**](RecordsApi.md#create_a_record) | **POST** /records | Create a Record
[**create_a_smart_import_record**](RecordsApi.md#create_a_smart_import_record) | **POST** /records/smart-import | Create a Smart Import Record
[**create_a_smart_import_record_to_import**](RecordsApi.md#create_a_smart_import_record_to_import) | **POST** /records/smart-import/{importId} | Upload a Smart Import Record to an existing Import
[**create_an_attachment_on_a_record**](RecordsApi.md#create_an_attachment_on_a_record) | **POST** /records/{id}/attachments/{key} | Create an Attachment on a Record
[**delete_a_record**](RecordsApi.md#delete_a_record) | **DELETE** /records/{id} | Delete a Record
[**delete_an_attachment_on_a_record**](RecordsApi.md#delete_an_attachment_on_a_record) | **DELETE** /records/{id}/attachments/{key} | Delete an Attachment on a Record
[**list_all_records**](RecordsApi.md#list_all_records) | **GET** /records | List All Records
[**list_all_records_metadata**](RecordsApi.md#list_all_records_metadata) | **GET** /records/metadata | Retrieve Records Schema
[**replace_a_record**](RecordsApi.md#replace_a_record) | **PUT** /records/{id} | Replace a Record
[**retrieve_a_record**](RecordsApi.md#retrieve_a_record) | **GET** /records/{id} | Retrieve a Record
[**retrieve_an_attachment_on_a_record**](RecordsApi.md#retrieve_an_attachment_on_a_record) | **GET** /records/{id}/attachments/{key} | Retrieve an Attachment on a Record
[**retrieve_import_predictions**](RecordsApi.md#retrieve_import_predictions) | **GET** /records/smart-import | Retrieve Predictions
[**retrieve_xlsx_export_file_of_all_records**](RecordsApi.md#retrieve_xlsx_export_file_of_all_records) | **GET** /records/export | Retrieve XLSX Export File of Records
[**update_record_metadata**](RecordsApi.md#update_record_metadata) | **PATCH** /records/{id} | Update Record Metadata


# **create_a_record**
> RecordModel create_a_record(create_a_record_request=create_a_record_request)

Create a Record

Create a contract record by specifying its intended metadata properties

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.create_a_record_request import CreateARecordRequest
from openapi_client.models.record_model import RecordModel
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
    api_instance = openapi_client.RecordsApi(api_client)
    create_a_record_request = openapi_client.CreateARecordRequest() # CreateARecordRequest |  (optional)

    try:
        # Create a Record
        api_response = api_instance.create_a_record(create_a_record_request=create_a_record_request)
        print("The response of RecordsApi->create_a_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->create_a_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_a_record_request** | [**CreateARecordRequest**](CreateARecordRequest.md)|  | [optional] 

### Return type

[**RecordModel**](RecordModel.md)

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

# **create_a_smart_import_record**
> CreateASmartImportRecord200Response create_a_smart_import_record(attachment, record_type=record_type, new_record_type_id=new_record_type_id, new_record_type_display_name=new_record_type_display_name)

Create a Smart Import Record

Upload a file to create a record with smart import and predictions.  Provide none of recordType, newRecordTypeId, or newRecordTypeDisplayName to default to Imported type.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.create_a_smart_import_record200_response import CreateASmartImportRecord200Response
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
    api_instance = openapi_client.RecordsApi(api_client)
    attachment = None # bytearray | Must be a binary. Base64 is not accepted at this time.
    record_type = 'imported' # str | Upload a smart import record as an existing record type.  Cannot provide alongside newRecordTypeId and newRecordTypeDisplayName. Defaults to Imported. (optional) (default to 'imported')
    new_record_type_id = 'new_record_type_id_example' # str | The record type ID for a not-yet-existing record type.  Must be provided along with a newRecordTypeDisplayName (optional)
    new_record_type_display_name = 'new_record_type_display_name_example' # str | The display name of the new record type to create. (optional)

    try:
        # Create a Smart Import Record
        api_response = api_instance.create_a_smart_import_record(attachment, record_type=record_type, new_record_type_id=new_record_type_id, new_record_type_display_name=new_record_type_display_name)
        print("The response of RecordsApi->create_a_smart_import_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->create_a_smart_import_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment** | **bytearray**| Must be a binary. Base64 is not accepted at this time. | 
 **record_type** | **str**| Upload a smart import record as an existing record type.  Cannot provide alongside newRecordTypeId and newRecordTypeDisplayName. Defaults to Imported. | [optional] [default to &#39;imported&#39;]
 **new_record_type_id** | **str**| The record type ID for a not-yet-existing record type.  Must be provided along with a newRecordTypeDisplayName | [optional] 
 **new_record_type_display_name** | **str**| The display name of the new record type to create. | [optional] 

### Return type

[**CreateASmartImportRecord200Response**](CreateASmartImportRecord200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |
**400** | 400 |  -  |
**403** | 403 |  -  |
**404** | 404 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_a_smart_import_record_to_import**
> CreateASmartImportRecord200Response create_a_smart_import_record_to_import(import_id, attachment, record_type, new_record_type_id=new_record_type_id, new_record_type_display_name=new_record_type_display_name)

Upload a Smart Import Record to an existing Import

Upload a file to an existing import and create a record with smart import and predictions.  Provide none of recordType, newRecordTypeId, or newRecordTypeDisplayName to default to Imported type.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.create_a_smart_import_record200_response import CreateASmartImportRecord200Response
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
    api_instance = openapi_client.RecordsApi(api_client)
    import_id = 'import_id_example' # str | The Import Id. You can upload a record to an existing import in the repository. 
    attachment = None # bytearray | Must be a binary. Base64 is not accepted at this time.
    record_type = 'imported' # str | Upload a smart import record as an existing record type.  Cannot provide alongside newRecordTypeId and newRecordTypeDisplayName. Defaults to Imported. (default to 'imported')
    new_record_type_id = 'new_record_type_id_example' # str | The record type ID for a not-yet-existing record type.  Must be provided along with a newRecordTypeDisplayName (optional)
    new_record_type_display_name = 'new_record_type_display_name_example' # str | The display name of the new record type to create. (optional)

    try:
        # Upload a Smart Import Record to an existing Import
        api_response = api_instance.create_a_smart_import_record_to_import(import_id, attachment, record_type, new_record_type_id=new_record_type_id, new_record_type_display_name=new_record_type_display_name)
        print("The response of RecordsApi->create_a_smart_import_record_to_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->create_a_smart_import_record_to_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The Import Id. You can upload a record to an existing import in the repository.  | 
 **attachment** | **bytearray**| Must be a binary. Base64 is not accepted at this time. | 
 **record_type** | **str**| Upload a smart import record as an existing record type.  Cannot provide alongside newRecordTypeId and newRecordTypeDisplayName. Defaults to Imported. | [default to &#39;imported&#39;]
 **new_record_type_id** | **str**| The record type ID for a not-yet-existing record type.  Must be provided along with a newRecordTypeDisplayName | [optional] 
 **new_record_type_display_name** | **str**| The display name of the new record type to create. | [optional] 

### Return type

[**CreateASmartImportRecord200Response**](CreateASmartImportRecord200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |
**400** | 400 |  -  |
**403** | 403 |  -  |
**404** | 404 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_an_attachment_on_a_record**
> object create_an_attachment_on_a_record(id, key, attachment=attachment, metadata=metadata)

Create an Attachment on a Record

Create an attachment on a specified record at the specified attachment key.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.create_an_attachment_on_a_record_request_metadata import CreateAnAttachmentOnARecordRequestMetadata
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
    api_instance = openapi_client.RecordsApi(api_client)
    id = 'id_example' # str | The ID or Ironclad ID of the Record. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api).
    key = 'signedCopy' # str | The attachment key. You can retrieve a list of available attachment keys with the [Retrieve Records Schema](https://developer.ironcladapp.com/reference/list-all-records-metadata) endpoint. (default to 'signedCopy')
    attachment = None # bytearray | Must be a binary. Base64 is not accepted at this time. (optional)
    metadata = openapi_client.CreateAnAttachmentOnARecordRequestMetadata() # CreateAnAttachmentOnARecordRequestMetadata |  (optional)

    try:
        # Create an Attachment on a Record
        api_response = api_instance.create_an_attachment_on_a_record(id, key, attachment=attachment, metadata=metadata)
        print("The response of RecordsApi->create_an_attachment_on_a_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->create_an_attachment_on_a_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or Ironclad ID of the Record. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api). | 
 **key** | **str**| The attachment key. You can retrieve a list of available attachment keys with the [Retrieve Records Schema](https://developer.ironcladapp.com/reference/list-all-records-metadata) endpoint. | [default to &#39;signedCopy&#39;]
 **attachment** | **bytearray**| Must be a binary. Base64 is not accepted at this time. | [optional] 
 **metadata** | [**CreateAnAttachmentOnARecordRequestMetadata**](CreateAnAttachmentOnARecordRequestMetadata.md)|  | [optional] 

### Return type

**object**

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |
**400** | Bad request error for creating record attachment. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_record**
> object delete_a_record(id)

Delete a Record

Delete an existing record

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
    api_instance = openapi_client.RecordsApi(api_client)
    id = 'id_example' # str | The ID or Ironclad ID of the Record.

    try:
        # Delete a Record
        api_response = api_instance.delete_a_record(id)
        print("The response of RecordsApi->delete_a_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->delete_a_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or Ironclad ID of the Record. | 

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
**204** | 204 |  -  |
**400** | 404 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_an_attachment_on_a_record**
> delete_an_attachment_on_a_record(id, key)

Delete an Attachment on a Record

Remove an attachment associated with a specific record

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
    api_instance = openapi_client.RecordsApi(api_client)
    id = 'id_example' # str | The ID or Ironclad ID of the Record.
    key = 'signedCopy' # str | The attachment key. (default to 'signedCopy')

    try:
        # Delete an Attachment on a Record
        api_instance.delete_an_attachment_on_a_record(id, key)
    except Exception as e:
        print("Exception when calling RecordsApi->delete_an_attachment_on_a_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or Ironclad ID of the Record. | 
 **key** | **str**| The attachment key. | [default to &#39;signedCopy&#39;]

### Return type

void (empty response body)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 |  -  |
**404** | Bad request error when deleting attachment. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_records**
> ListAllRecords200Response list_all_records(page=page, page_size=page_size, types=types, last_updated=last_updated, filter=filter, sort_field=sort_field, sort_direction=sort_direction)

List All Records

View all records in the company, with filtering available via query parameters

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.list_all_records200_response import ListAllRecords200Response
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
    api_instance = openapi_client.RecordsApi(api_client)
    page = 0 # int | The page number used when paginating through a list of results. (optional) (default to 0)
    page_size = 20 # int | A limit of the number of results to return. (optional) (default to 20)
    types = 'mutualNDA,consultingAgreement' # str | Comma separated (no spaces) record types to export. Use the [Retrieve Records Schema](https://developer.ironcladapp.com/reference/list-all-records-metadata) endpoint to retrieve a list of types. (optional)
    last_updated = '2018-03-10T00:00:00.000Z' # str | Get records updated since (UTC) (optional)
    filter = 'Equals([counterpartyName], \'Test LLC\')' # str | Filter records for those that contain (1) the specified property with (2) the specified value. The record property ID should be enclosed in brackets `[ ]` and the value should be enclosed in single quotes `' '`. (optional)
    sort_field = agreementDate # str | The field to sort Records. Only one field is supported in the sort operation. (optional) (default to agreementDate)
    sort_direction = DESC # str | The direction the records are sorted by in correlation with the `sortField`. (optional) (default to DESC)

    try:
        # List All Records
        api_response = api_instance.list_all_records(page=page, page_size=page_size, types=types, last_updated=last_updated, filter=filter, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of RecordsApi->list_all_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->list_all_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number used when paginating through a list of results. | [optional] [default to 0]
 **page_size** | **int**| A limit of the number of results to return. | [optional] [default to 20]
 **types** | **str**| Comma separated (no spaces) record types to export. Use the [Retrieve Records Schema](https://developer.ironcladapp.com/reference/list-all-records-metadata) endpoint to retrieve a list of types. | [optional] 
 **last_updated** | **str**| Get records updated since (UTC) | [optional] 
 **filter** | **str**| Filter records for those that contain (1) the specified property with (2) the specified value. The record property ID should be enclosed in brackets &#x60;[ ]&#x60; and the value should be enclosed in single quotes &#x60;&#39; &#39;&#x60;. | [optional] 
 **sort_field** | **str**| The field to sort Records. Only one field is supported in the sort operation. | [optional] [default to agreementDate]
 **sort_direction** | **str**| The direction the records are sorted by in correlation with the &#x60;sortField&#x60;. | [optional] [default to DESC]

### Return type

[**ListAllRecords200Response**](ListAllRecords200Response.md)

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

# **list_all_records_metadata**
> ListAllRecordsMetadata200Response list_all_records_metadata()

Retrieve Records Schema

View the schema associated with contract records, including available record types and metadata properties.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.list_all_records_metadata200_response import ListAllRecordsMetadata200Response
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
    api_instance = openapi_client.RecordsApi(api_client)

    try:
        # Retrieve Records Schema
        api_response = api_instance.list_all_records_metadata()
        print("The response of RecordsApi->list_all_records_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->list_all_records_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAllRecordsMetadata200Response**](ListAllRecordsMetadata200Response.md)

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

# **replace_a_record**
> RecordModel replace_a_record(id, replace_a_record_request=replace_a_record_request)

Replace a Record

Update an existing record with a new set of metadata

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.record_model import RecordModel
from openapi_client.models.replace_a_record_request import ReplaceARecordRequest
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
    api_instance = openapi_client.RecordsApi(api_client)
    id = 'id_example' # str | The ID or Ironclad ID of the Record.
    replace_a_record_request = openapi_client.ReplaceARecordRequest() # ReplaceARecordRequest |  (optional)

    try:
        # Replace a Record
        api_response = api_instance.replace_a_record(id, replace_a_record_request=replace_a_record_request)
        print("The response of RecordsApi->replace_a_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->replace_a_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or Ironclad ID of the Record. | 
 **replace_a_record_request** | [**ReplaceARecordRequest**](ReplaceARecordRequest.md)|  | [optional] 

### Return type

[**RecordModel**](RecordModel.md)

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

# **retrieve_a_record**
> RecordModel retrieve_a_record(id)

Retrieve a Record

View a specific record and its associated data

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.record_model import RecordModel
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
    api_instance = openapi_client.RecordsApi(api_client)
    id = 'id_example' # str | The ID or Ironclad ID of the Record.

    try:
        # Retrieve a Record
        api_response = api_instance.retrieve_a_record(id)
        print("The response of RecordsApi->retrieve_a_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->retrieve_a_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or Ironclad ID of the Record. | 

### Return type

[**RecordModel**](RecordModel.md)

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

# **retrieve_an_attachment_on_a_record**
> object retrieve_an_attachment_on_a_record(id, key)

Retrieve an Attachment on a Record

View an attachment associated with a specific record

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
    api_instance = openapi_client.RecordsApi(api_client)
    id = 'id_example' # str | The ID or Ironclad ID of the Record.
    key = 'signedCopy' # str | The attachment key. (default to 'signedCopy')

    try:
        # Retrieve an Attachment on a Record
        api_response = api_instance.retrieve_an_attachment_on_a_record(id, key)
        print("The response of RecordsApi->retrieve_an_attachment_on_a_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->retrieve_an_attachment_on_a_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or Ironclad ID of the Record. | 
 **key** | **str**| The attachment key. | [default to &#39;signedCopy&#39;]

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

# **retrieve_import_predictions**
> RetrieveImportPredictions200Response retrieve_import_predictions(record_id=record_id, import_id=import_id)

Retrieve Predictions

Retrieve status of predictions of specific smart import record or all records in an import, one of Record Id or Import Id is required.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.retrieve_import_predictions200_response import RetrieveImportPredictions200Response
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
    api_instance = openapi_client.RecordsApi(api_client)
    record_id = 'record_id_example' # str | The ID of the Record for prediction status. (optional)
    import_id = 'import_id_example' # str | The ID of the Import for prediction statuses. (optional)

    try:
        # Retrieve Predictions
        api_response = api_instance.retrieve_import_predictions(record_id=record_id, import_id=import_id)
        print("The response of RecordsApi->retrieve_import_predictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->retrieve_import_predictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**| The ID of the Record for prediction status. | [optional] 
 **import_id** | **str**| The ID of the Import for prediction statuses. | [optional] 

### Return type

[**RetrieveImportPredictions200Response**](RetrieveImportPredictions200Response.md)

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
**403** | 403 |  -  |
**404** | 404 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_xlsx_export_file_of_all_records**
> object retrieve_xlsx_export_file_of_all_records(types=types, properties=properties)

Retrieve XLSX Export File of Records

Export a records report with filtering available via query parameters

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
    api_instance = openapi_client.RecordsApi(api_client)
    types = 'types_example' # str | Comma separated list of record types to export. Example: `mutualNDA,NDA` (optional)
    properties = 'properties_example' # str | IDs of properties to export, comma separated. Example: `counterpartyName,agreementDate` (optional)

    try:
        # Retrieve XLSX Export File of Records
        api_response = api_instance.retrieve_xlsx_export_file_of_all_records(types=types, properties=properties)
        print("The response of RecordsApi->retrieve_xlsx_export_file_of_all_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->retrieve_xlsx_export_file_of_all_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | **str**| Comma separated list of record types to export. Example: &#x60;mutualNDA,NDA&#x60; | [optional] 
 **properties** | **str**| IDs of properties to export, comma separated. Example: &#x60;counterpartyName,agreementDate&#x60; | [optional] 

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

# **update_record_metadata**
> RecordModel update_record_metadata(id, update_record_metadata_request=update_record_metadata_request)

Update Record Metadata

Update specific fields on a record

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.record_model import RecordModel
from openapi_client.models.update_record_metadata_request import UpdateRecordMetadataRequest
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
    api_instance = openapi_client.RecordsApi(api_client)
    id = 'id_example' # str | The ID or Ironclad ID of the Record.
    update_record_metadata_request = {"type":"consultingAgreement","name":"Consulting Agreement with Jane Doe","addProperties":{"agreementDate":{"type":"date","value":"2018-05-08T00:00:00-07:00"},"counterpartyName":{"type":"string","value":"Jane Doe"}},"removeProperties":["counterpartySigner"],"addLinks":[{"recordId":"df1c2805-f5a3-4a14-9386-c28d950dff49"}],"removeLinks":[{"recordId":"df1c2805-f5a3-4a14-9386-c28d950dff49"}]} # UpdateRecordMetadataRequest |  (optional)

    try:
        # Update Record Metadata
        api_response = api_instance.update_record_metadata(id, update_record_metadata_request=update_record_metadata_request)
        print("The response of RecordsApi->update_record_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->update_record_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or Ironclad ID of the Record. | 
 **update_record_metadata_request** | [**UpdateRecordMetadataRequest**](UpdateRecordMetadataRequest.md)|  | [optional] 

### Return type

[**RecordModel**](RecordModel.md)

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
**404** | 404 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

