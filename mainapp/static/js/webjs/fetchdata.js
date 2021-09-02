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

/**
 * Escape HTML XSS
 * @param {*} unsafe_str 
 * @returns 
 */
function escapeHTML(unsafe_str) {
    return unsafe_str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\"/g, '&quot;')
    .replace(/\'/g, '&#39;')
    .replace(/\//g, '&#x2F;')
}