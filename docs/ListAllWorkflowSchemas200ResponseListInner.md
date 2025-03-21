# ListAllWorkflowSchemas200ResponseListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**var_schema** | [**UpdateWorkflowMetadata200ResponseSchema**](UpdateWorkflowMetadata200ResponseSchema.md) |  | [optional] 
**permissions** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.list_all_workflow_schemas200_response_list_inner import ListAllWorkflowSchemas200ResponseListInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllWorkflowSchemas200ResponseListInner from a JSON string
list_all_workflow_schemas200_response_list_inner_instance = ListAllWorkflowSchemas200ResponseListInner.from_json(json)
# print the JSON string representation of the object
print(ListAllWorkflowSchemas200ResponseListInner.to_json())

# convert the object into a dict
list_all_workflow_schemas200_response_list_inner_dict = list_all_workflow_schemas200_response_list_inner_instance.to_dict()
# create an instance of ListAllWorkflowSchemas200ResponseListInner from a dict
list_all_workflow_schemas200_response_list_inner_from_dict = ListAllWorkflowSchemas200ResponseListInner.from_dict(list_all_workflow_schemas200_response_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


