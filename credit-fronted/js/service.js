import axios from 'axios';

'use strict';

/**
 * util service to get data from api 
 */

let service =(()=>{

    const URLAPI = "http://127.0.0.1:5000/api/v1/";

   
    /**
     * Returns a list of service
     *
     * @function
     * @param {string} moduleIds List of dom-module id's within which to
     * search for css.
     * @return {!Array<!HTMLStyleElement>} Array of contained <style> elements
     * @this {StyleGather}
     */

    let postListElements = (url,data,auto='')=>{
        console.log(`${URLAPI}${url}`)
        console.log(data)
        axios.post(`${URLAPI}${url}`, data)
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });
    }

    let getListElements = (url,auto='')=>{
        console.log("get")
    }
    

    return{
        URLAPI,
        getListElements,
        postListElements
    };

})();

export default service;