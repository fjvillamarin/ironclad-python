# WorkflowAsyncLaunchSuccessResponseWorkflowUrls



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser_url** | **str** | The URL for accessing the workflow in a browser. | [optional] [readonly] 
**api_url** | **str** | The URL for accessing workflow data via the REST API. | [optional] [readonly] 

## Example

```python
from openapi_client.models.workflow_async_launch_success_response_workflow_urls import WorkflowAsyncLaunchSuccessResponseWorkflowUrls

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowAsyncLaunchSuccessResponseWorkflowUrls from a JSON string
workflow_async_launch_success_response_workflow_urls_instance = WorkflowAsyncLaunchSuccessResponseWorkflowUrls.from_json(json)
# print the JSON string representation of the object
print(WorkflowAsyncLaunchSuccessResponseWorkflowUrls.to_json())

# convert the object into a dict
workflow_async_launch_success_response_workflow_urls_dict = workflow_async_launch_success_response_workflow_urls_instance.to_dict()
# create an instance of WorkflowAsyncLaunchSuccessResponseWorkflowUrls from a dict
workflow_async_launch_success_response_workflow_urls_from_dict = WorkflowAsyncLaunchSuccessResponseWorkflowUrls.from_dict(workflow_async_launch_success_response_workflow_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


