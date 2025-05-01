# API

## V1

### Meter

Types:

```python
from meterhub.types.api.v1 import MeterAnalyzeResponse, MeterDetectResponse
```

Methods:

- <code title="post /api/v1/meter/analyze/">client.api.v1.meter.<a href="./src/meterhub/resources/api/v1/meter/meter.py">analyze</a>(\*\*<a href="src/meterhub/types/api/v1/meter_analyze_params.py">params</a>) -> <a href="./src/meterhub/types/api/v1/meter_analyze_response.py">MeterAnalyzeResponse</a></code>
- <code title="post /api/v1/meter/detect/">client.api.v1.meter.<a href="./src/meterhub/resources/api/v1/meter/meter.py">detect</a>(\*\*<a href="src/meterhub/types/api/v1/meter_detect_params.py">params</a>) -> <a href="./src/meterhub/types/api/v1/meter_detect_response.py">MeterDetectResponse</a></code>

#### Read

Types:

```python
from meterhub.types.api.v1.meter import MeterReading
```

Methods:

- <code title="post /api/v1/meter/read/">client.api.v1.meter.read.<a href="./src/meterhub/resources/api/v1/meter/read.py">retrieve</a>(\*\*<a href="src/meterhub/types/api/v1/meter/read_retrieve_params.py">params</a>) -> <a href="./src/meterhub/types/api/v1/meter/meter_reading.py">MeterReading</a></code>
- <code title="post /api/v1/meter/read/dataset">client.api.v1.meter.read.<a href="./src/meterhub/resources/api/v1/meter/read.py">dataset</a>(\*\*<a href="src/meterhub/types/api/v1/meter/read_dataset_params.py">params</a>) -> <a href="./src/meterhub/types/api/v1/meter/meter_reading.py">MeterReading</a></code>
