# BaseActivityFeedItemModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**metadata** | [**ActivityMetadataModel**](ActivityMetadataModel.md) |  | 
**author** | [**ActivityAuthorModel**](ActivityAuthorModel.md) |  | 
**is_external** | **bool** |  | [optional] 
**reactions** | [**ActivityReactionModel**](ActivityReactionModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.base_activity_feed_item_model import BaseActivityFeedItemModel

# TODO update the JSON string below
json = "{}"
# create an instance of BaseActivityFeedItemModel from a JSON string
base_activity_feed_item_model_instance = BaseActivityFeedItemModel.from_json(json)
# print the JSON string representation of the object
print(BaseActivityFeedItemModel.to_json())

# convert the object into a dict
base_activity_feed_item_model_dict = base_activity_feed_item_model_instance.to_dict()
# create an instance of BaseActivityFeedItemModel from a dict
base_activity_feed_item_model_from_dict = BaseActivityFeedItemModel.from_dict(base_activity_feed_item_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


