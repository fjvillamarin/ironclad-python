# CreatorModel

The Ironclad user (must be a user in your Ironclad account) to be used for launching the workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of value used to identify the user. | [optional] [default to 'id']
**email** | **str** | The email address of the Ironclad user. | [optional] 
**id** | **str** | The user ID of the Ironclad user. | [optional] 

## Example

```python
from openapi_client.models.creator_model import CreatorModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreatorModel from a JSON string
creator_model_instance = CreatorModel.from_json(json)
# print the JSON string representation of the object
print(CreatorModel.to_json())

# convert the object into a dict
creator_model_dict = creator_model_instance.to_dict()
# create an instance of CreatorModel from a dict
creator_model_from_dict = CreatorModel.from_dict(creator_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


