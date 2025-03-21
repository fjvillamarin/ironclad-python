# RetrieveAWorkflowSchema200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**var_schema** | [**UpdateWorkflowMetadata200ResponseSchema**](UpdateWorkflowMetadata200ResponseSchema.md) |  | [optional] 
**permissions** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.retrieve_a_workflow_schema200_response import RetrieveAWorkflowSchema200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAWorkflowSchema200Response from a JSON string
retrieve_a_workflow_schema200_response_instance = RetrieveAWorkflowSchema200Response.from_json(json)
# print the JSON string representation of the object
print(RetrieveAWorkflowSchema200Response.to_json())

# convert the object into a dict
retrieve_a_workflow_schema200_response_dict = retrieve_a_workflow_schema200_response_instance.to_dict()
# create an instance of RetrieveAWorkflowSchema200Response from a dict
retrieve_a_workflow_schema200_response_from_dict = RetrieveAWorkflowSchema200Response.from_dict(retrieve_a_workflow_schema200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


