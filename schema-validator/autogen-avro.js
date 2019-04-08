const fs = require('fs');
const avro = require('avsc');

const testMeta = require('./test_meta.json')

testMeta['test_names'].forEach((tn) => {
  console.log(tn)
  let datum = JSON.parse(fs.readFileSync(`test-specs/${tn}.json`).toString());

  let inferredType = avro.Type.forValue(datum['test_keys'])

  let dst = `schemas/${tn}.avsc`
  fs.writeFileSync(dst, JSON.stringify(inferredType.schema(), {}, 2))
})


