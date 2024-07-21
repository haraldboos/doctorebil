import { useState } from 'react';

import request from '../axio/request';
import PropTypes from 'prop-types';

import Button from '@mui/material/Button';

// const Ssmmss = async(event,value)=>{
//     let sms=await (smsmessage,smsmessage)=>{


//     }
//     return sms.data;

// }
export default  function SSmms({message,smsnumber}){
    const [loading, setLoading] = useState(false);

    if (!message || !smsnumber) {
        // Handle case where 'message' or 'smsnumber' is not provided
        return <div>Message or SMS number not provided</div>;
    }
    console.log(typeof(smsnumber));

    const smssend = async()=>{
        setLoading(true)
        try{ 
            const requstsms=await request.sendsms(message,smsnumber);
            console.log(requstsms);
        }catch(eerror){
            console.error(eerror);
            setLoading(false)
        }
       
    }
    
    return(
        <Button variant="contained" onClick={smssend}><h1>{loading ? 'Sending...' : 'Click to send SMS'}</h1></Button>

    )
}
SSmms.propTypes = {
    message: PropTypes.string.isRequired, // Ensure 'message' prop is a required string
    smsnumber: PropTypes.number.isRequired // Ensure 'smsnumber' prop is a required string
  };