import React, { useEffect, useState } from 'react';

function SiLoButton(){
    const accessToken = localStorage.getItem('token');
    var buttonValue ="";
    if(accessToken==''){
        buttonValue = "Sign In";       
        console.log('access token pusty');
        }
        else
        {
            buttonValue="Sign Out"
                console.log(accessToken);
        }
    const handleButtonClick=()=>{

        if(accessToken==''){
            window.location.href='/Login';
        }
        else{
            localStorage.setItem('token', '');
        }
    };

return(
    <div>
    <button onClick={handleButtonClick}>{buttonValue}</button>
    </div> 
);
}
export default SiLoButton;