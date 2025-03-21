# UpdateWorkflowMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[UpdateWorkflowMetadataRequestUpdatesInner]**](UpdateWorkflowMetadataRequestUpdatesInner.md) |  | 
**comment** | **str** | A comment that explains the updates you are making to the workflow. | [optional] 

## Example

```python
from openapi_client.models.update_workflow_metadata_request import UpdateWorkflowMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkflowMetadataRequest from a JSON string
update_workflow_metadata_request_instance = UpdateWorkflowMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkflowMetadataRequest.to_json())

# convert the object into a dict
update_workflow_metadata_request_dict = update_workflow_metadata_request_instance.to_dict()
# create an instance of UpdateWorkflowMetadataRequest from a dict
update_workflow_metadata_request_from_dict = UpdateWorkflowMetadataRequest.from_dict(update_workflow_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


