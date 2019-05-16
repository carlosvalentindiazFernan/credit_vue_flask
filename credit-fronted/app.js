import axios from 'axios';
import service from './js/service.js'
(function login(){
    'use strict';
    const email = document.querySelector('#exampleInputEmail1');
    const password = document.querySelector('#exampleInputPassword1')
    const btn = document.querySelector('#btnSubtmit')
    const BASE_URL = '';

    const res =  axios.get(BASE_URL)
                    .then( data => console.log(data))
    
    
    console.log(`GET: Here's the list of todos`, res);
    
    btn.addEventListener('click',(e)=>{
        console.log(email.value)
        console.log(password.value)    
        console.log(service.URLAPI)
        let d =service.getListElements('login/',{
            'email':email,
            'passoword': password
        })

        console.log(d)

    });

})();