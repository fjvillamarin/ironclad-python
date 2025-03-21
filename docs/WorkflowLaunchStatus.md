# WorkflowLaunchStatus

The current status of the launch workflow job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [readonly] [default to 'in_progress']
**request_payload** | [**WorkflowRequestModel**](WorkflowRequestModel.md) |  | 
**workflow_urls** | [**WorkflowAsyncLaunchSuccessResponseWorkflowUrls**](WorkflowAsyncLaunchSuccessResponseWorkflowUrls.md) |  | 
**workflow** | [**LaunchedWorkflowModel**](LaunchedWorkflowModel.md) |  | 
**error** | **str** | An error message indicating why the workflow failed to launch. | [readonly] 

## Example

```python
from openapi_client.models.workflow_launch_status import WorkflowLaunchStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowLaunchStatus from a JSON string
workflow_launch_status_instance = WorkflowLaunchStatus.from_json(json)
# print the JSON string representation of the object
print(WorkflowLaunchStatus.to_json())

# convert the object into a dict
workflow_launch_status_dict = workflow_launch_status_instance.to_dict()
# create an instance of WorkflowLaunchStatus from a dict
workflow_launch_status_from_dict = WorkflowLaunchStatus.from_dict(workflow_launch_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


