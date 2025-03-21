# WorkflowAsyncInProgressResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [readonly] [default to 'in_progress']
**request_payload** | [**WorkflowRequestModel**](WorkflowRequestModel.md) |  | 

## Example

```python
from openapi_client.models.workflow_async_in_progress_response import WorkflowAsyncInProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowAsyncInProgressResponse from a JSON string
workflow_async_in_progress_response_instance = WorkflowAsyncInProgressResponse.from_json(json)
# print the JSON string representation of the object
print(WorkflowAsyncInProgressResponse.to_json())

# convert the object into a dict
workflow_async_in_progress_response_dict = workflow_async_in_progress_response_instance.to_dict()
# create an instance of WorkflowAsyncInProgressResponse from a dict
workflow_async_in_progress_response_from_dict = WorkflowAsyncInProgressResponse.from_dict(workflow_async_in_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


