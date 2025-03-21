# CreateARecordRequestPropertiesAgreementDate

The date of the agreement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'date']
**value** | **str** | UTC date (e.g. &#x60;2018-05-08T00:00:00-07:00&#x60;) | [optional] 

## Example

```python
from openapi_client.models.create_a_record_request_properties_agreement_date import CreateARecordRequestPropertiesAgreementDate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateARecordRequestPropertiesAgreementDate from a JSON string
create_a_record_request_properties_agreement_date_instance = CreateARecordRequestPropertiesAgreementDate.from_json(json)
# print the JSON string representation of the object
print(CreateARecordRequestPropertiesAgreementDate.to_json())

# convert the object into a dict
create_a_record_request_properties_agreement_date_dict = create_a_record_request_properties_agreement_date_instance.to_dict()
# create an instance of CreateARecordRequestPropertiesAgreementDate from a dict
create_a_record_request_properties_agreement_date_from_dict = CreateARecordRequestPropertiesAgreementDate.from_dict(create_a_record_request_properties_agreement_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


