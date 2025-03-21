# openapi_client.WorkflowsApi

All URIs are relative to *https://ironcladapp.com/public/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approval_requests**](WorkflowsApi.md#approval_requests) | **GET** /workflows/{id}/approval-requests | Retrieve the Approval Requests on a Workflow
[**create_a_comment_on_a_workflow**](WorkflowsApi.md#create_a_comment_on_a_workflow) | **POST** /workflows/{id}/comments | Create a Comment on a Workflow
[**create_a_new_workflow_async**](WorkflowsApi.md#create_a_new_workflow_async) | **POST** /workflows/async | Create a Workflow Asynchronously
[**deprecated_create_a_comment_on_a_workflow**](WorkflowsApi.md#deprecated_create_a_comment_on_a_workflow) | **POST** /workflows/{id}/comment | Create a Comment on a Workflow
[**launch_a_new_workflow**](WorkflowsApi.md#launch_a_new_workflow) | **POST** /workflows | Create a Workflow Synchronously
[**list_all_workflow_approvals**](WorkflowsApi.md#list_all_workflow_approvals) | **GET** /workflows/{id}/approvals | List All Workflow Approvals
[**list_all_workflow_participants**](WorkflowsApi.md#list_all_workflow_participants) | **GET** /workflows/{id}/participants | List All Workflow Participants
[**list_all_workflow_schemas**](WorkflowsApi.md#list_all_workflow_schemas) | **GET** /workflow-schemas | List All Workflow Schemas
[**list_all_workflow_signers**](WorkflowsApi.md#list_all_workflow_signers) | **GET** /workflows/{id}/signatures | List All Workflow Signers
[**list_all_workflows**](WorkflowsApi.md#list_all_workflows) | **GET** /workflows | List All Workflows
[**retrieve_a_workflow**](WorkflowsApi.md#retrieve_a_workflow) | **GET** /workflows/{id} | Retrieve a Workflow
[**retrieve_a_workflow_document**](WorkflowsApi.md#retrieve_a_workflow_document) | **GET** /workflows/{id}/document/{key}/download | Retrieve a Workflow Document
[**retrieve_a_workflow_schema**](WorkflowsApi.md#retrieve_a_workflow_schema) | **GET** /workflow-schemas/{id} | Retrieve a Workflow Schema
[**retrieve_asynchronous_workflow_status**](WorkflowsApi.md#retrieve_asynchronous_workflow_status) | **GET** /workflows/async/{asyncJobId} | Retrieve the Status of an Async Workflow Create Job
[**retrieve_attachment_from_email_thread**](WorkflowsApi.md#retrieve_attachment_from_email_thread) | **GET** /workflows/{id}/emails/{emailThreadId}/attachments/{attachmentId} | Retrieve an Attachment from an Email Thread
[**retrieve_email_thread_from_workflow**](WorkflowsApi.md#retrieve_email_thread_from_workflow) | **GET** /workflows/{id}/emails/{emailThreadId} | Retrieve an Email Thread from a Specified Workflow
[**retrieve_email_threads_from_workflow**](WorkflowsApi.md#retrieve_email_threads_from_workflow) | **GET** /workflows/{id}/emails | Retrieve Email Threads from A Workflow
[**revert_to_review**](WorkflowsApi.md#revert_to_review) | **PATCH** /workflows/{id}/revert-to-review | Revert a Workflow to the Review Step
[**turn_history**](WorkflowsApi.md#turn_history) | **GET** /workflows/{id}/turn-history | Retrieve the Turn History on a Workflow
[**update_workflow_approval**](WorkflowsApi.md#update_workflow_approval) | **PATCH** /workflows/{id}/approvals/{roleId} | Update Approval on a Workflow
[**update_workflow_metadata**](WorkflowsApi.md#update_workflow_metadata) | **PATCH** /workflows/{id}/attributes | Update Workflow Metadata


# **approval_requests**
> ApprovalRequests200Response approval_requests(id, page=page, page_size=page_size, actor_details=actor_details)

Retrieve the Approval Requests on a Workflow

Returns a list of approval requests that have taken place on the workflow.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.approval_requests200_response import ApprovalRequests200Response
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'id_example' # str | The unique identifier or Ironclad ID of a workflow.
    page = 0 # int | The page number used when paginating through a list of results. (optional) (default to 0)
    page_size = 20 # int | A limit of the number of results to return. (optional) (default to 20)
    actor_details = False # bool | An optional boolean parameter that adds additional information about the actor to each item in the response. Defaults to false. (optional) (default to False)

    try:
        # Retrieve the Approval Requests on a Workflow
        api_response = api_instance.approval_requests(id, page=page, page_size=page_size, actor_details=actor_details)
        print("The response of WorkflowsApi->approval_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->approval_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier or Ironclad ID of a workflow. | 
 **page** | **int**| The page number used when paginating through a list of results. | [optional] [default to 0]
 **page_size** | **int**| A limit of the number of results to return. | [optional] [default to 20]
 **actor_details** | **bool**| An optional boolean parameter that adds additional information about the actor to each item in the response. Defaults to false. | [optional] [default to False]

### Return type

[**ApprovalRequests200Response**](ApprovalRequests200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |
**404** | 404 |  -  |
**403** | 403 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_a_comment_on_a_workflow**
> CommentActivityModel create_a_comment_on_a_workflow(id, deprecated_create_a_comment_on_a_workflow_request=deprecated_create_a_comment_on_a_workflow_request)

Create a Comment on a Workflow

Creates a comment in the specified workflow's activity feed.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.comment_activity_model import CommentActivityModel
from openapi_client.models.deprecated_create_a_comment_on_a_workflow_request import DeprecatedCreateACommentOnAWorkflowRequest
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'id_example' # str | The unique identifier or Ironclad ID of a workflow.
    deprecated_create_a_comment_on_a_workflow_request = openapi_client.DeprecatedCreateACommentOnAWorkflowRequest() # DeprecatedCreateACommentOnAWorkflowRequest |  (optional)

    try:
        # Create a Comment on a Workflow
        api_response = api_instance.create_a_comment_on_a_workflow(id, deprecated_create_a_comment_on_a_workflow_request=deprecated_create_a_comment_on_a_workflow_request)
        print("The response of WorkflowsApi->create_a_comment_on_a_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->create_a_comment_on_a_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier or Ironclad ID of a workflow. | 
 **deprecated_create_a_comment_on_a_workflow_request** | [**DeprecatedCreateACommentOnAWorkflowRequest**](DeprecatedCreateACommentOnAWorkflowRequest.md)|  | [optional] 

### Return type

[**CommentActivityModel**](CommentActivityModel.md)

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

# **create_a_new_workflow_async**
> CreateANewWorkflowAsync200Response create_a_new_workflow_async(workflow_request_model=workflow_request_model)

Create a Workflow Asynchronously

Launch a new Workflow asynchronously for non-blocking performance, which is helpful when/if you provide files to the Workflow.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.create_a_new_workflow_async200_response import CreateANewWorkflowAsync200Response
from openapi_client.models.workflow_request_model import WorkflowRequestModel
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    workflow_request_model = openapi_client.WorkflowRequestModel() # WorkflowRequestModel |  (optional)

    try:
        # Create a Workflow Asynchronously
        api_response = api_instance.create_a_new_workflow_async(workflow_request_model=workflow_request_model)
        print("The response of WorkflowsApi->create_a_new_workflow_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->create_a_new_workflow_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_request_model** | [**WorkflowRequestModel**](WorkflowRequestModel.md)|  | [optional] 

### Return type

[**CreateANewWorkflowAsync200Response**](CreateANewWorkflowAsync200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response of the initiated async workflow launch. |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deprecated_create_a_comment_on_a_workflow**
> object deprecated_create_a_comment_on_a_workflow(id, deprecated_create_a_comment_on_a_workflow_request=deprecated_create_a_comment_on_a_workflow_request)

Create a Comment on a Workflow

Creates a comment in the specified workflow's activity feed.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.deprecated_create_a_comment_on_a_workflow_request import DeprecatedCreateACommentOnAWorkflowRequest
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'id_example' # str | The unique identifier or Ironclad ID of a workflow.
    deprecated_create_a_comment_on_a_workflow_request = openapi_client.DeprecatedCreateACommentOnAWorkflowRequest() # DeprecatedCreateACommentOnAWorkflowRequest |  (optional)

    try:
        # Create a Comment on a Workflow
        api_response = api_instance.deprecated_create_a_comment_on_a_workflow(id, deprecated_create_a_comment_on_a_workflow_request=deprecated_create_a_comment_on_a_workflow_request)
        print("The response of WorkflowsApi->deprecated_create_a_comment_on_a_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->deprecated_create_a_comment_on_a_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier or Ironclad ID of a workflow. | 
 **deprecated_create_a_comment_on_a_workflow_request** | [**DeprecatedCreateACommentOnAWorkflowRequest**](DeprecatedCreateACommentOnAWorkflowRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 |  -  |
**400** | 400 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_a_new_workflow**
> LaunchedWorkflowModel launch_a_new_workflow(workflow_request_model=workflow_request_model)

Create a Workflow Synchronously

Launch a new Workflow synchronously.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.launched_workflow_model import LaunchedWorkflowModel
from openapi_client.models.workflow_request_model import WorkflowRequestModel
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    workflow_request_model = openapi_client.WorkflowRequestModel() # WorkflowRequestModel |  (optional)

    try:
        # Create a Workflow Synchronously
        api_response = api_instance.launch_a_new_workflow(workflow_request_model=workflow_request_model)
        print("The response of WorkflowsApi->launch_a_new_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->launch_a_new_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_request_model** | [**WorkflowRequestModel**](WorkflowRequestModel.md)|  | [optional] 

### Return type

[**LaunchedWorkflowModel**](LaunchedWorkflowModel.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Launched Workflow Response. |  -  |
**400** | Error Launching Workflow. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_workflow_approvals**
> ListAllWorkflowApprovals200Response list_all_workflow_approvals(id)

List All Workflow Approvals

Returns a list of approvals for the workflow. The `approvalGroups` property will display only triggered approvals (i.e. conditional approvals that have not been triggered will not appear).

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.list_all_workflow_approvals200_response import ListAllWorkflowApprovals200Response
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'abcd1234' # str | The unique identifier or Ironclad ID of a workflow.

    try:
        # List All Workflow Approvals
        api_response = api_instance.list_all_workflow_approvals(id)
        print("The response of WorkflowsApi->list_all_workflow_approvals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->list_all_workflow_approvals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier or Ironclad ID of a workflow. | 

### Return type

[**ListAllWorkflowApprovals200Response**](ListAllWorkflowApprovals200Response.md)

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

# **list_all_workflow_participants**
> ListAllWorkflowParticipants200Response list_all_workflow_participants(id, page=page, page_size=page_size, email=email)

List All Workflow Participants

Returns a list of workflow participants.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.list_all_workflow_participants200_response import ListAllWorkflowParticipants200Response
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'id_example' # str | The unique identifier or Ironclad ID of a workflow.
    page = 0 # int | The page number used when paginating through a list of results. (optional) (default to 0)
    page_size = 20 # int | A limit of the number of results to return. (optional) (default to 20)
    email = 'email_example' # str | The Ironclad user's email address. (optional)

    try:
        # List All Workflow Participants
        api_response = api_instance.list_all_workflow_participants(id, page=page, page_size=page_size, email=email)
        print("The response of WorkflowsApi->list_all_workflow_participants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->list_all_workflow_participants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier or Ironclad ID of a workflow. | 
 **page** | **int**| The page number used when paginating through a list of results. | [optional] [default to 0]
 **page_size** | **int**| A limit of the number of results to return. | [optional] [default to 20]
 **email** | **str**| The Ironclad user&#39;s email address. | [optional] 

### Return type

[**ListAllWorkflowParticipants200Response**](ListAllWorkflowParticipants200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |
**403** | 403 |  -  |
**404** | 404 not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_workflow_schemas**
> ListAllWorkflowSchemas200Response list_all_workflow_schemas(form, x_as_user_email=x_as_user_email, x_as_user_id=x_as_user_id)

List All Workflow Schemas

Returns a list of workflow schemas. Each schema specifies the fields used in the workflow's launch form.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.list_all_workflow_schemas200_response import ListAllWorkflowSchemas200Response
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    form = 'launch' # str | The launch form is the only form supported at this time. (default to 'launch')
    x_as_user_email = 'jane.doe@test.com' # str | Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions (optional)
    x_as_user_id = '5f0375c4cdc1927a3c5edcd3' # str | Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions (optional)

    try:
        # List All Workflow Schemas
        api_response = api_instance.list_all_workflow_schemas(form, x_as_user_email=x_as_user_email, x_as_user_id=x_as_user_id)
        print("The response of WorkflowsApi->list_all_workflow_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->list_all_workflow_schemas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form** | **str**| The launch form is the only form supported at this time. | [default to &#39;launch&#39;]
 **x_as_user_email** | **str**| Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions | [optional] 
 **x_as_user_id** | **str**| Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions | [optional] 

### Return type

[**ListAllWorkflowSchemas200Response**](ListAllWorkflowSchemas200Response.md)

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

# **list_all_workflow_signers**
> ListAllWorkflowSigners200Response list_all_workflow_signers(id)

List All Workflow Signers

Returns a list of workflow signers and the status of their signature.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.list_all_workflow_signers200_response import ListAllWorkflowSigners200Response
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'id_example' # str | The unique identifier or Ironclad ID of a workflow.

    try:
        # List All Workflow Signers
        api_response = api_instance.list_all_workflow_signers(id)
        print("The response of WorkflowsApi->list_all_workflow_signers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->list_all_workflow_signers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier or Ironclad ID of a workflow. | 

### Return type

[**ListAllWorkflowSigners200Response**](ListAllWorkflowSigners200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_workflows**
> ListAllWorkflows200Response list_all_workflows(page=page, page_size=page_size, status=status, template=template, last_updated=last_updated, filter=filter)

List All Workflows

List all workflows in your Ironclad account.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.list_all_workflows200_response import ListAllWorkflows200Response
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    page = 0 # int | The page number used when paginating through a list of results. (optional) (default to 0)
    page_size = 20 # int | A limit of the number of results to return. (optional) (default to 20)
    status = 'status_example' # str | Filter the workflows that are listed based on their status. If this parameter is omitted, `active` workflows will be returned. Active workflows include workflows in the Create, Review, Sign, and Archive stages. (optional)
    template = 'template_example' # str | Filter workflows to a specific Template ID. (optional)
    last_updated = 'last_updated_example' # str | Retrieve workflows that have been updated since a UTC date. (optional)
    filter = 'Equals([counterpartyName], \'Harley Quinn\')' # str | Filter workflows using a formula. The workflow attribute ID should be enclosed in brackets `[ ]` and the value should be enclosed in single quotes `' '`.  Workflow attributes for a specific workflow design can be identified using the [List All Workflow Schemas](https://developer.ironcladapp.com/reference/list-all-workflow-schemas) endpoint.  Supported formula operations include:  <ul>   <li><code>Equals</code></li>   <li><code>Contains</code></li>   <li><code>And</code></li>   <li><code>Or</code></li> </ul> For more information on writing formulas, please refer to <a href=\"https://ironcladapp.com/formulas/#company%20display%20name\">this article</a>. (optional)

    try:
        # List All Workflows
        api_response = api_instance.list_all_workflows(page=page, page_size=page_size, status=status, template=template, last_updated=last_updated, filter=filter)
        print("The response of WorkflowsApi->list_all_workflows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->list_all_workflows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number used when paginating through a list of results. | [optional] [default to 0]
 **page_size** | **int**| A limit of the number of results to return. | [optional] [default to 20]
 **status** | **str**| Filter the workflows that are listed based on their status. If this parameter is omitted, &#x60;active&#x60; workflows will be returned. Active workflows include workflows in the Create, Review, Sign, and Archive stages. | [optional] 
 **template** | **str**| Filter workflows to a specific Template ID. | [optional] 
 **last_updated** | **str**| Retrieve workflows that have been updated since a UTC date. | [optional] 
 **filter** | **str**| Filter workflows using a formula. The workflow attribute ID should be enclosed in brackets &#x60;[ ]&#x60; and the value should be enclosed in single quotes &#x60;&#39; &#39;&#x60;.  Workflow attributes for a specific workflow design can be identified using the [List All Workflow Schemas](https://developer.ironcladapp.com/reference/list-all-workflow-schemas) endpoint.  Supported formula operations include:  &lt;ul&gt;   &lt;li&gt;&lt;code&gt;Equals&lt;/code&gt;&lt;/li&gt;   &lt;li&gt;&lt;code&gt;Contains&lt;/code&gt;&lt;/li&gt;   &lt;li&gt;&lt;code&gt;And&lt;/code&gt;&lt;/li&gt;   &lt;li&gt;&lt;code&gt;Or&lt;/code&gt;&lt;/li&gt; &lt;/ul&gt; For more information on writing formulas, please refer to &lt;a href&#x3D;\&quot;https://ironcladapp.com/formulas/#company%20display%20name\&quot;&gt;this article&lt;/a&gt;. | [optional] 

### Return type

[**ListAllWorkflows200Response**](ListAllWorkflows200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_a_workflow**
> WorkflowResponseModel retrieve_a_workflow(id)

Retrieve a Workflow

View the data associated with a specific workflow

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.workflow_response_model import WorkflowResponseModel
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'abcd1234' # str | The unique identifier or Ironclad ID of a workflow.

    try:
        # Retrieve a Workflow
        api_response = api_instance.retrieve_a_workflow(id)
        print("The response of WorkflowsApi->retrieve_a_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->retrieve_a_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier or Ironclad ID of a workflow. | 

### Return type

[**WorkflowResponseModel**](WorkflowResponseModel.md)

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

# **retrieve_a_workflow_document**
> object retrieve_a_workflow_document(id, key)

Retrieve a Workflow Document

Download a document associated with a specific workflow via a reference to its document key

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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'id_example' # str | The unique identifier or Ironclad ID of a workflow.
    key = 'key_example' # str | The unique identifier for the attachment. This key can be located using the [Retrieve a Workflow](https://developer.ironcladapp.com/reference/retrieve-a-workflow) endpoint. In the response, locate the file attribute (e.g., `draft`) and look at its `download` parameter. The download parameter includes the key at the end of the URL `.../document/{ATTACHMENT_KEY}/download`

    try:
        # Retrieve a Workflow Document
        api_response = api_instance.retrieve_a_workflow_document(id, key)
        print("The response of WorkflowsApi->retrieve_a_workflow_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->retrieve_a_workflow_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier or Ironclad ID of a workflow. | 
 **key** | **str**| The unique identifier for the attachment. This key can be located using the [Retrieve a Workflow](https://developer.ironcladapp.com/reference/retrieve-a-workflow) endpoint. In the response, locate the file attribute (e.g., &#x60;draft&#x60;) and look at its &#x60;download&#x60; parameter. The download parameter includes the key at the end of the URL &#x60;.../document/{ATTACHMENT_KEY}/download&#x60; | 

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

# **retrieve_a_workflow_schema**
> RetrieveAWorkflowSchema200Response retrieve_a_workflow_schema(id, form=form, x_as_user_email=x_as_user_email, x_as_user_id=x_as_user_id)

Retrieve a Workflow Schema

Returns the fields used in the workflow's launch form.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.retrieve_a_workflow_schema200_response import RetrieveAWorkflowSchema200Response
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'id_example' # str | The unique identifier of a schema (see explanation of [Template ID](https://developer.ironcladapp.com/reference/getting-started-api)). A list of identifiers can be retrieved using the `GET /workflow-schemas` endpoint. Only published workflows will have an identifier. 
    form = 'launch' # str |  (optional) (default to 'launch')
    x_as_user_email = 'jane.doe@test.com' # str | Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions (optional)
    x_as_user_id = '5f0375c4cdc1927a3c5edcd3' # str | Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions (optional)

    try:
        # Retrieve a Workflow Schema
        api_response = api_instance.retrieve_a_workflow_schema(id, form=form, x_as_user_email=x_as_user_email, x_as_user_id=x_as_user_id)
        print("The response of WorkflowsApi->retrieve_a_workflow_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->retrieve_a_workflow_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of a schema (see explanation of [Template ID](https://developer.ironcladapp.com/reference/getting-started-api)). A list of identifiers can be retrieved using the &#x60;GET /workflow-schemas&#x60; endpoint. Only published workflows will have an identifier.  | 
 **form** | **str**|  | [optional] [default to &#39;launch&#39;]
 **x_as_user_email** | **str**| Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions | [optional] 
 **x_as_user_id** | **str**| Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions | [optional] 

### Return type

[**RetrieveAWorkflowSchema200Response**](RetrieveAWorkflowSchema200Response.md)

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

# **retrieve_asynchronous_workflow_status**
> WorkflowLaunchStatus retrieve_asynchronous_workflow_status(async_job_id)

Retrieve the Status of an Async Workflow Create Job

Check the status of a Workflow you created while using the [Create a Workflow Async](https://developer.ironcladapp.com/reference/create-a-workflow-sync-vs-async#create-a-new-workflow-async) route.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.workflow_launch_status import WorkflowLaunchStatus
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    async_job_id = 'async_job_id_example' # str | The identifier provided in the response of creating a Workflow asynchronously.

    try:
        # Retrieve the Status of an Async Workflow Create Job
        api_response = api_instance.retrieve_asynchronous_workflow_status(async_job_id)
        print("The response of WorkflowsApi->retrieve_asynchronous_workflow_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->retrieve_asynchronous_workflow_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_job_id** | **str**| The identifier provided in the response of creating a Workflow asynchronously. | 

### Return type

[**WorkflowLaunchStatus**](WorkflowLaunchStatus.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of the workflow launch. |  -  |
**404** | 404 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_attachment_from_email_thread**
> object retrieve_attachment_from_email_thread(id, email_thread_id, attachment_id)

Retrieve an Attachment from an Email Thread

Retrieve an attachment from the specified email thread

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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'id_example' # str | The unique identifier of a workflow
    email_thread_id = 'email_thread_id_example' # str | The unique identifier of an email thread
    attachment_id = 'attachment_id_example' # str | The unique identifier for the attachment. This key can be located using the [Retrieve email threads from workflow](https://developer.ironcladapp.com/reference/retrieve-emails) endpoint. In the response, locate the file attribute (e.g., `attachments`) and look at its `download` parameter. The download parameter includes the key at the end of the URL `...emails/{emailThreadId}/attachment/{ATTACHMENT_ID}`

    try:
        # Retrieve an Attachment from an Email Thread
        api_response = api_instance.retrieve_attachment_from_email_thread(id, email_thread_id, attachment_id)
        print("The response of WorkflowsApi->retrieve_attachment_from_email_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->retrieve_attachment_from_email_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of a workflow | 
 **email_thread_id** | **str**| The unique identifier of an email thread | 
 **attachment_id** | **str**| The unique identifier for the attachment. This key can be located using the [Retrieve email threads from workflow](https://developer.ironcladapp.com/reference/retrieve-emails) endpoint. In the response, locate the file attribute (e.g., &#x60;attachments&#x60;) and look at its &#x60;download&#x60; parameter. The download parameter includes the key at the end of the URL &#x60;...emails/{emailThreadId}/attachment/{ATTACHMENT_ID}&#x60; | 

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
**404** | 404 not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_email_thread_from_workflow**
> EmailResponseModel retrieve_email_thread_from_workflow(id, email_thread_id)

Retrieve an Email Thread from a Specified Workflow

List a single email thread for a specified workflow

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.email_response_model import EmailResponseModel
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'id_example' # str | The unique identifier of a workflow
    email_thread_id = 'email_thread_id_example' # str | The unique identifier of an email thread

    try:
        # Retrieve an Email Thread from a Specified Workflow
        api_response = api_instance.retrieve_email_thread_from_workflow(id, email_thread_id)
        print("The response of WorkflowsApi->retrieve_email_thread_from_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->retrieve_email_thread_from_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of a workflow | 
 **email_thread_id** | **str**| The unique identifier of an email thread | 

### Return type

[**EmailResponseModel**](EmailResponseModel.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET Email Response |  -  |
**404** | 404 not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_email_threads_from_workflow**
> RetrieveEmailThreadsFromWorkflow200Response retrieve_email_threads_from_workflow(id, page=page, page_size=page_size)

Retrieve Email Threads from A Workflow

List all email threads in the specified workflow

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.retrieve_email_threads_from_workflow200_response import RetrieveEmailThreadsFromWorkflow200Response
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'id_example' # str | The unique identifier of a workflow
    page = 0 # int | The page number used when paginating through a list of results. (optional) (default to 0)
    page_size = 20 # int | A limit of the number of results to return. (optional) (default to 20)

    try:
        # Retrieve Email Threads from A Workflow
        api_response = api_instance.retrieve_email_threads_from_workflow(id, page=page, page_size=page_size)
        print("The response of WorkflowsApi->retrieve_email_threads_from_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->retrieve_email_threads_from_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of a workflow | 
 **page** | **int**| The page number used when paginating through a list of results. | [optional] [default to 0]
 **page_size** | **int**| A limit of the number of results to return. | [optional] [default to 20]

### Return type

[**RetrieveEmailThreadsFromWorkflow200Response**](RetrieveEmailThreadsFromWorkflow200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET Emails Response. |  -  |
**404** | 404 not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_to_review**
> revert_to_review(id, x_as_user_email=x_as_user_email, x_as_user_id=x_as_user_id, revert_to_review_request=revert_to_review_request)

Revert a Workflow to the Review Step

Reverts a workflow to the Review step. Only workflows sourced from Workflow Designer and in the Sign step can be reverted.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.revert_to_review_request import RevertToReviewRequest
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'id_example' # str | The unique identifier or Ironclad ID of a workflow.
    x_as_user_email = 'jane.doe@test.com' # str | Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions (optional)
    x_as_user_id = '5f0375c4cdc1927a3c5edcd3' # str | Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions (optional)
    revert_to_review_request = openapi_client.RevertToReviewRequest() # RevertToReviewRequest |  (optional)

    try:
        # Revert a Workflow to the Review Step
        api_instance.revert_to_review(id, x_as_user_email=x_as_user_email, x_as_user_id=x_as_user_id, revert_to_review_request=revert_to_review_request)
    except Exception as e:
        print("Exception when calling WorkflowsApi->revert_to_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier or Ironclad ID of a workflow. | 
 **x_as_user_email** | **str**| Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions | [optional] 
 **x_as_user_id** | **str**| Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions | [optional] 
 **revert_to_review_request** | [**RevertToReviewRequest**](RevertToReviewRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 |  -  |
**400** | 400 |  -  |
**403** | 403 |  -  |
**404** | 404 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **turn_history**
> TurnHistory200Response turn_history(id, page=page, page_size=page_size)

Retrieve the Turn History on a Workflow

An array of objects for each turn on a workflow.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.turn_history200_response import TurnHistory200Response
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'id_example' # str | The unique identifier or Ironclad ID of a workflow.
    page = 0 # int | The page number used when paginating through a list of results. (optional) (default to 0)
    page_size = 20 # int | A limit of the number of results to return. (optional) (default to 20)

    try:
        # Retrieve the Turn History on a Workflow
        api_response = api_instance.turn_history(id, page=page, page_size=page_size)
        print("The response of WorkflowsApi->turn_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->turn_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier or Ironclad ID of a workflow. | 
 **page** | **int**| The page number used when paginating through a list of results. | [optional] [default to 0]
 **page_size** | **int**| A limit of the number of results to return. | [optional] [default to 20]

### Return type

[**TurnHistory200Response**](TurnHistory200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |
**404** | 404 |  -  |
**403** | 403 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workflow_approval**
> bool update_workflow_approval(id, role_id, update_workflow_approval_request=update_workflow_approval_request)

Update Approval on a Workflow

Updates an approval to the specified status. Approvals can only be updated during the Review step.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.update_workflow_approval_request import UpdateWorkflowApprovalRequest
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'abcd1234' # str | The unique identifier or Ironclad ID of a workflow.
    role_id = 'role_id_example' # str | The unique identifier of the approver role whose status should be changed. This identifier can be retrieved using the `GET /workflows/{id}/approvals` endpoint.
    update_workflow_approval_request = openapi_client.UpdateWorkflowApprovalRequest() # UpdateWorkflowApprovalRequest |  (optional)

    try:
        # Update Approval on a Workflow
        api_response = api_instance.update_workflow_approval(id, role_id, update_workflow_approval_request=update_workflow_approval_request)
        print("The response of WorkflowsApi->update_workflow_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->update_workflow_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier or Ironclad ID of a workflow. | 
 **role_id** | **str**| The unique identifier of the approver role whose status should be changed. This identifier can be retrieved using the &#x60;GET /workflows/{id}/approvals&#x60; endpoint. | 
 **update_workflow_approval_request** | [**UpdateWorkflowApprovalRequest**](UpdateWorkflowApprovalRequest.md)|  | [optional] 

### Return type

**bool**

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

# **update_workflow_metadata**
> UpdateWorkflowMetadata200Response update_workflow_metadata(id, x_as_user_email=x_as_user_email, x_as_user_id=x_as_user_id, update_workflow_metadata_request=update_workflow_metadata_request)

Update Workflow Metadata

The workflow must be in the Review step in order for its data to be updated. Use the `remove` action to clear field values and the `set` action to add or modify values. Form validation is enforced; required fields cannot be removed and any required fields triggered by conditions must be populated.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.update_workflow_metadata200_response import UpdateWorkflowMetadata200Response
from openapi_client.models.update_workflow_metadata_request import UpdateWorkflowMetadataRequest
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
    api_instance = openapi_client.WorkflowsApi(api_client)
    id = 'id_example' # str | The unique identifier or Ironclad ID of a workflow.
    x_as_user_email = 'jane.doe@test.com' # str | Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions (optional)
    x_as_user_id = '5f0375c4cdc1927a3c5edcd3' # str | Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions (optional)
    update_workflow_metadata_request = openapi_client.UpdateWorkflowMetadataRequest() # UpdateWorkflowMetadataRequest |  (optional)

    try:
        # Update Workflow Metadata
        api_response = api_instance.update_workflow_metadata(id, x_as_user_email=x_as_user_email, x_as_user_id=x_as_user_id, update_workflow_metadata_request=update_workflow_metadata_request)
        print("The response of WorkflowsApi->update_workflow_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->update_workflow_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier or Ironclad ID of a workflow. | 
 **x_as_user_email** | **str**| Filters the list of workflow schemas based on the permissions of a user associated with the specified user email. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions | [optional] 
 **x_as_user_id** | **str**| Filters the list of workflow schemas based on the permissions of a user associated with the specified user id. Permissions can be launch, view, or both. Corresponds to the permissions here: https://support.ironcladapp.com/s/article/Understanding-and-Managing-Permissions | [optional] 
 **update_workflow_metadata_request** | [**UpdateWorkflowMetadataRequest**](UpdateWorkflowMetadataRequest.md)|  | [optional] 

### Return type

[**UpdateWorkflowMetadata200Response**](UpdateWorkflowMetadata200Response.md)

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
**403** | 403 |  -  |
**404** | 404 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

