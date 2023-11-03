import { createElement, useEffect, useState } from 'react'
import { ENV } from './config';
import './App.css'

function App() {
  const [loading, setLoading] = useState(false);

  const createForm = (e) => {
    e.preventDefault();
    const firstName = document.querySelector("#firstName").value;
    const lastName = document.querySelector("#lastName").value;
    const amount = document.querySelector("#amount").value;

    setLoading(true)
    fetch(`${ENV.URL}/paymentForm`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json;charset=UTF-8",
        "Access-Control-Allow-Origin": "*"
      },
      body: JSON.stringify({ firstName, lastName, amount })
    })
      .then(res => res.json())
      .then(json => {
        console.log(json);
        const form = document.createElement("form");
        form.method = "POST";
        form.action = ENV.URL_PAYMENT;
        for (let key in json) {
          if (json.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.type = 'hidden';
            hiddenField.name = key;
            hiddenField.value = json[key];

            form.appendChild(hiddenField);
          }
        }
        const submitButton = document.createElement("input");
        submitButton.type = 'submit';
        submitButton.value = 'Submit';
        submitButton.style.display = "none";

        form.appendChild(submitButton);
        document.body.appendChild(form);
        submitButton.click();
      })
      .catch(err => console.log(err))
  }


  return (
    <>
      <form className='container' onSubmit={createForm}>
        <input id='firstName' type='text' placeholder='first name' required />
        <input id='lastName' type='text' placeholder='last name' required />
        <input id='amount' type='number' placeholder='amount' required />
        {!loading ? (<input type='submit' value="Pagar" />) : (
          <div className="spinner-border text-danger" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        )}

      </form>


    </>
  )
}

export default App
