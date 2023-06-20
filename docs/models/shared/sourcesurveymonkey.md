# SourceSurveymonkey

The values required to configure the source.


## Fields

| Field                                                                                                                                                     | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               | Example                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `credentials`                                                                                                                                             | [Optional[SourceSurveymonkeySurveyMonkeyAuthorizationMethod]](../../models/shared/sourcesurveymonkeysurveymonkeyauthorizationmethod.md)                   | :heavy_minus_sign:                                                                                                                                        | The authorization method to use to retrieve data from SurveyMonkey                                                                                        |                                                                                                                                                           |
| `origin`                                                                                                                                                  | [Optional[SourceSurveymonkeyOriginDatacenterOfTheSurveyMonkeyAccount]](../../models/shared/sourcesurveymonkeyorigindatacenterofthesurveymonkeyaccount.md) | :heavy_minus_sign:                                                                                                                                        | Depending on the originating datacenter of the SurveyMonkey account, the API access URL may be different.                                                 |                                                                                                                                                           |
| `source_type`                                                                                                                                             | [SourceSurveymonkeySurveymonkey](../../models/shared/sourcesurveymonkeysurveymonkey.md)                                                                   | :heavy_check_mark:                                                                                                                                        | N/A                                                                                                                                                       |                                                                                                                                                           |
| `start_date`                                                                                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                      | :heavy_check_mark:                                                                                                                                        | UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated.                                                   | 2021-01-01T00:00:00Z                                                                                                                                      |
| `survey_ids`                                                                                                                                              | list[*str*]                                                                                                                                               | :heavy_minus_sign:                                                                                                                                        | IDs of the surveys from which you'd like to replicate data. If left empty, data from all boards to which you have access will be replicated.              |                                                                                                                                                           |