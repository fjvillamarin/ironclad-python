# WorkflowAsyncLaunchSuccessResponse

Response for a successfully asynchronously launched workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [readonly] [default to 'success']
**request_payload** | [**WorkflowRequestModel**](WorkflowRequestModel.md) |  | 
**workflow_urls** | [**WorkflowAsyncLaunchSuccessResponseWorkflowUrls**](WorkflowAsyncLaunchSuccessResponseWorkflowUrls.md) |  | 
**workflow** | [**LaunchedWorkflowModel**](LaunchedWorkflowModel.md) |  | 

## Example

```python
from openapi_client.models.workflow_async_launch_success_response import WorkflowAsyncLaunchSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowAsyncLaunchSuccessResponse from a JSON string
workflow_async_launch_success_response_instance = WorkflowAsyncLaunchSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(WorkflowAsyncLaunchSuccessResponse.to_json())

# convert the object into a dict
workflow_async_launch_success_response_dict = workflow_async_launch_success_response_instance.to_dict()
# create an instance of WorkflowAsyncLaunchSuccessResponse from a dict
workflow_async_launch_success_response_from_dict = WorkflowAsyncLaunchSuccessResponse.from_dict(workflow_async_launch_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


