import axios from 'axios';
import service from './js/service.js'

(function login() {
    'use strict';

    const email = document.querySelector('#exampleInputEmail1');
    const password = document.querySelector('#exampleInputPassword1')
    const btn = document.querySelector('#btnSubtmit')

    const listCredit = document.querySelector('#listCredits')

    /**
     * Create Credit
     */
    const formCreate = document.querySelector('#formCreate')
    const companyInput = document.querySelector('#companyInput')
    const companyNumberInput = document.querySelector('#companyNumberInput')
    const creditInput = document.querySelector('#creditInput')
    const btnSubtmitCreate = document.querySelector('#btnSubtmitCreate')


    if (btn) {
        btn.addEventListener('click', (e) => {
            axios.post(`${service.URLAPI}login/`, {
                'email': email.value,
                'password': password.value
            })
                .then(data => dataLogin(data))
                .catch(e => console.error('error login'))
        });
    }


    let dataLogin = (data) => {
        if (service.isvalidStatus(data.status)) {
            window.location.href = '/menu.html'
            service.setToken(data.data)
        } else {
            console.error("Error status")
        }
    }

    if (listCredit) {
        axios
            .get(`${service.URLAPI}credits/`, {
                headers: {
                    Authorization: service.getToken()
                }
            })
            .then(response => {
                const {data:{data}} = response
                if(data.length > 0){
                    data.forEach(element =>{
                        let li = document.createElement('li');
                        li.setAttribute('class','list-group-item');
                        listCredit.appendChild(li);
                        li.textContent= `Id ${element.id} 
                        Company ${element.nameCompany} - ${element.numCompany}  
                        Credit $${element.credit}`;
                    })
                }

            })
            .catch(error => {
                console.error('An error occurred:', error);
            });
    }

    if (formCreate) {        
        btnSubtmitCreate.addEventListener('click', (e) => {
            let data = {
                'nameCompany': companyInput.value,
                'numberCompany': companyNumberInput.value,
                'credit': creditInput.value,
            }

            let headerConfig = {
                headers: {
                    Authorization: service.getToken()
                }    
            }
    
            axios
                .post(`${service.URLAPI}credits/`, data,headerConfig)
                .then(response => {
                    if(service.isCreated(response.status)){
                        window.location.href = '/menu.html'                        
                    }
                })
                .catch(error => {
                    alert(error)
                    console.error('An error occurred:', error);
                });

        });
    }

})();