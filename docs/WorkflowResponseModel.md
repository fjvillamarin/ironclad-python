# WorkflowResponseModel

The response from a successful workflow retrieval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**ironclad_id** | **str** |  | [optional] 
**title** | **str** |  | 
**template** | **str** |  | 
**step** | **str** |  | 
**var_schema** | [**UpdateWorkflowMetadata200ResponseSchema**](UpdateWorkflowMetadata200ResponseSchema.md) |  | 
**attributes** | [**WorkflowResponseModelAttributes**](WorkflowResponseModelAttributes.md) |  | 
**is_cancelled** | **bool** |  | [default to True]
**is_complete** | **bool** |  | [default to True]
**status** | **str** |  | 
**creator** | [**WorkflowResponseModelCreator**](WorkflowResponseModelCreator.md) |  | [optional] 
**created** | **str** |  | 
**last_updated** | **str** |  | 
**roles** | [**List[WorkflowResponseModelRolesInner]**](WorkflowResponseModelRolesInner.md) |  | 
**approvals** | [**WorkflowStateModel**](WorkflowStateModel.md) |  | 
**signatures** | [**WorkflowStateModel**](WorkflowStateModel.md) |  | 
**record_ids** | **List[str]** |  | [optional] 
**is_revertible_to_review** | **bool** |  | 

## Example

```python
from openapi_client.models.workflow_response_model import WorkflowResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowResponseModel from a JSON string
workflow_response_model_instance = WorkflowResponseModel.from_json(json)
# print the JSON string representation of the object
print(WorkflowResponseModel.to_json())

# convert the object into a dict
workflow_response_model_dict = workflow_response_model_instance.to_dict()
# create an instance of WorkflowResponseModel from a dict
workflow_response_model_from_dict = WorkflowResponseModel.from_dict(workflow_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


