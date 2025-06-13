const apiKey = pm.environment.get("POSTMAN_API_KEY");
const envId = pm.environment.get("POSTMAN_ENV_ID");
const keyName = "MY_SECRET";
const value = "my-dynamic-secret";

const body = {
  "values": [
    {
      "key": keyName,
      "value": value,
      "enabled": true
    }
  ]
};

pm.sendRequest({
  url: `https://api.getpostman.com/environments/${envId}`,
  method: 'PUT',
  header: {
    'X-Api-Key': apiKey,
    'Content-Type': 'application/json'
  },
  body: {
    mode: 'raw',
    raw: JSON.stringify(body)
  }
}, function (err, res) {
  console.log("Updated Initial Value for", keyName);
});