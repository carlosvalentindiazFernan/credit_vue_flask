import axios from 'axios';

'use strict';

/**
 * util service to get data from api 
 */

let service =(()=>{

    const URLAPI = "http://127.0.0.1:5000/api/v1/";
    let auth_token = ""

    let getToken = (data)=>{
        if (isvalidStatus(data.status)){
            auth_token = data.data
            return auth_token
        }else{
            auth_token = ""
            return auth_token
        }
    }

    let isvalidStatus = (status) =>{
        return (status == 200)? true : false
    }

    return{
        getToken,
        isvalidStatus,
        URLAPI
    };

})();

export default service;