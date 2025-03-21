# ActivityReactionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emoji_id** | **str** |  | [optional] 
**reactors** | [**List[UserModel]**](UserModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.activity_reaction_model import ActivityReactionModel

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityReactionModel from a JSON string
activity_reaction_model_instance = ActivityReactionModel.from_json(json)
# print the JSON string representation of the object
print(ActivityReactionModel.to_json())

# convert the object into a dict
activity_reaction_model_dict = activity_reaction_model_instance.to_dict()
# create an instance of ActivityReactionModel from a dict
activity_reaction_model_from_dict = ActivityReactionModel.from_dict(activity_reaction_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


