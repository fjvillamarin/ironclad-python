# ListAllWorkflowSchemas400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**param** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.list_all_workflow_schemas400_response import ListAllWorkflowSchemas400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllWorkflowSchemas400Response from a JSON string
list_all_workflow_schemas400_response_instance = ListAllWorkflowSchemas400Response.from_json(json)
# print the JSON string representation of the object
print(ListAllWorkflowSchemas400Response.to_json())

# convert the object into a dict
list_all_workflow_schemas400_response_dict = list_all_workflow_schemas400_response_instance.to_dict()
# create an instance of ListAllWorkflowSchemas400Response from a dict
list_all_workflow_schemas400_response_from_dict = ListAllWorkflowSchemas400Response.from_dict(list_all_workflow_schemas400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


