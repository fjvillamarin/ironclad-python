# LaunchedWorkflowModel

The response from a successful workflow launch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the launched workflow. | [readonly] 
**ironclad_id** | **str** | The Ironclad ID of the launched workflow. | [optional] [readonly] 
**title** | **str** | The name used for the launched workflow. | [readonly] 
**template** | **str** | The identifier of the workflow template | 
**step** | **str** | The step the workflow is currently on. | [readonly] 
**var_schema** | [**AttributesModel**](AttributesModel.md) |  | 
**is_cancelled** | **bool** | Displays if the launched workflow has been cancelled. | [readonly] 
**is_complete** | **bool** | Displays if the launched workflow has been completed. | [readonly] 
**status** | **str** | The current status of the launched workflow. | [readonly] 
**creator** | [**LaunchedWorkflowModelCreator**](LaunchedWorkflowModelCreator.md) |  | [optional] 
**created** | **str** | The date (ISO8601 format) the workflow was launched | [readonly] 
**last_updated** | **str** | The date (ISO8601 format) the workflow was last updated | [readonly] 
**roles** | [**List[WorkflowRoleModel]**](WorkflowRoleModel.md) |  | [readonly] 
**approvals** | [**LaunchedWorkflowModelApprovals**](LaunchedWorkflowModelApprovals.md) |  | 
**signatures** | [**LaunchedWorkflowModelSignatures**](LaunchedWorkflowModelSignatures.md) |  | 
**record_ids** | **List[str]** |  | [optional] [readonly] 
**is_revertible_to_review** | **bool** | Displays if the launched workflow can be reverted back to the review step. | [readonly] 

## Example

```python
from openapi_client.models.launched_workflow_model import LaunchedWorkflowModel

# TODO update the JSON string below
json = "{}"
# create an instance of LaunchedWorkflowModel from a JSON string
launched_workflow_model_instance = LaunchedWorkflowModel.from_json(json)
# print the JSON string representation of the object
print(LaunchedWorkflowModel.to_json())

# convert the object into a dict
launched_workflow_model_dict = launched_workflow_model_instance.to_dict()
# create an instance of LaunchedWorkflowModel from a dict
launched_workflow_model_from_dict = LaunchedWorkflowModel.from_dict(launched_workflow_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


