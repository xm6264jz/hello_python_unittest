


module.exports = (req, res, next) => {

  console.log('req', req.query)

  const _send = res.send;

  res.send = function(body){

    let params = require('url').parse(req.originalUrl, true)
    let t = params.query['t'];
    let title = params.query['title'];
    let key = params.query['apikey']

    if (!key) {
      let no_key = {
        "Response": "False",
        "Error": "No API key provided."
      }
      return _send.call(this, JSON.stringify(no_key));
    }

    let jsonResponse = JSON.parse(body)

    if (Array.isArray(jsonResponse)) {
      if (jsonResponse.length === 1) {
        return _send.call(this, JSON.stringify(jsonResponse[0]))
      }

      else if (jsonResponse.length === 0) {

        let not_found =  {
          "Response":"False",
          "Error": "Movie not found!"
        }

        return _send.call(this, JSON.stringify(not_found))
      }
    }

    return _send.call(this, JSON.stringify(jsonResponse))
  }
  
  next();

}

// credit to https://github.com/typicode/json-server/issues/541
