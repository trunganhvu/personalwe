/**
 * call api method get
 * @param {string} api 
 * @returns response
 */
function fetchApi(api){
    // Fetch data from api
    const response = fetch(api)
    .then(function(response) {
        if(!response.ok) throw new Error("HTTP error, status = " + response.status);
        let myjson_data = response.json();
        return myjson_data;
    })
    .then(function(mydata){
        // If size data = 0 return message
        if (Object.keys(mydata).length == 0){
            return {'message': ''};
        }
        else { // Size data > 0
            return mydata;
        }
    })
    .catch(function(error) {
        return {'message': 'error'};
    })
    return response;
}