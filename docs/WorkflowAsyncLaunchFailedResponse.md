# WorkflowAsyncLaunchFailedResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [readonly] [default to 'failed']
**request_payload** | [**WorkflowRequestModel**](WorkflowRequestModel.md) |  | 
**error** | **str** | An error message indicating why the workflow failed to launch. | [readonly] 

## Example

```python
from openapi_client.models.workflow_async_launch_failed_response import WorkflowAsyncLaunchFailedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowAsyncLaunchFailedResponse from a JSON string
workflow_async_launch_failed_response_instance = WorkflowAsyncLaunchFailedResponse.from_json(json)
# print the JSON string representation of the object
print(WorkflowAsyncLaunchFailedResponse.to_json())

# convert the object into a dict
workflow_async_launch_failed_response_dict = workflow_async_launch_failed_response_instance.to_dict()
# create an instance of WorkflowAsyncLaunchFailedResponse from a dict
workflow_async_launch_failed_response_from_dict = WorkflowAsyncLaunchFailedResponse.from_dict(workflow_async_launch_failed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


