# UpdateWorkflowMetadataRequestUpdatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The type of action you&#39;d like to take on an existing attribute (read-only fields cannot be updated). Use the remove action to clear values. If using the remove action, the attribute cannot be required by the workflow. | [default to 'set']
**path** | **str** | The workflow attribute id that you&#39;d like to make a change to. Workflow attribute IDs and values can be retrieved using the [Retrieve a Workflow](https://developer.ironcladapp.com/reference/retrieve-a-workflow) endpoint. | 
**value** | **str** | The value to change the attribute to. Only required when the &#x60;action&#x60; property is &#x60;set&#x60; and not &#x60;remove&#x60;. The value&#39;s format must conform to the field type (e.g., &#x60;\&quot;someString\&quot;&#x60; for strings, &#x60;true&#x60; or &#x60;false&#x60; for booleans, etc. | [optional] 

## Example

```python
from openapi_client.models.update_workflow_metadata_request_updates_inner import UpdateWorkflowMetadataRequestUpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkflowMetadataRequestUpdatesInner from a JSON string
update_workflow_metadata_request_updates_inner_instance = UpdateWorkflowMetadataRequestUpdatesInner.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkflowMetadataRequestUpdatesInner.to_json())

# convert the object into a dict
update_workflow_metadata_request_updates_inner_dict = update_workflow_metadata_request_updates_inner_instance.to_dict()
# create an instance of UpdateWorkflowMetadataRequestUpdatesInner from a dict
update_workflow_metadata_request_updates_inner_from_dict = UpdateWorkflowMetadataRequestUpdatesInner.from_dict(update_workflow_metadata_request_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


