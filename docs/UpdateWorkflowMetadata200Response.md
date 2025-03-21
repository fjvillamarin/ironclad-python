# UpdateWorkflowMetadata200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**ironclad_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**step** | **str** |  | [optional] 
**var_schema** | [**UpdateWorkflowMetadata200ResponseSchema**](UpdateWorkflowMetadata200ResponseSchema.md) |  | [optional] 
**attributes** | [**UpdateWorkflowMetadata200ResponseAttributes**](UpdateWorkflowMetadata200ResponseAttributes.md) |  | [optional] 
**is_cancelled** | **bool** |  | [optional] [default to True]
**is_complete** | **bool** |  | [optional] [default to True]
**status** | **str** |  | [optional] 
**creator** | [**UpdateWorkflowMetadata200ResponseCreator**](UpdateWorkflowMetadata200ResponseCreator.md) |  | [optional] 
**created** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**roles** | [**List[ListAllWorkflowApprovals200ResponseRolesInner]**](ListAllWorkflowApprovals200ResponseRolesInner.md) |  | [optional] 
**approvals** | [**UpdateWorkflowMetadata200ResponseApprovals**](UpdateWorkflowMetadata200ResponseApprovals.md) |  | [optional] 
**signatures** | [**UpdateWorkflowMetadata200ResponseSignatures**](UpdateWorkflowMetadata200ResponseSignatures.md) |  | [optional] 
**record_ids** | **List[str]** |  | [optional] 
**is_revertible_to_review** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.update_workflow_metadata200_response import UpdateWorkflowMetadata200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkflowMetadata200Response from a JSON string
update_workflow_metadata200_response_instance = UpdateWorkflowMetadata200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkflowMetadata200Response.to_json())

# convert the object into a dict
update_workflow_metadata200_response_dict = update_workflow_metadata200_response_instance.to_dict()
# create an instance of UpdateWorkflowMetadata200Response from a dict
update_workflow_metadata200_response_from_dict = UpdateWorkflowMetadata200Response.from_dict(update_workflow_metadata200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


