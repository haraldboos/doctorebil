import { useEffect, useState } from "react";
import IconButton from "@mui/material/IconButton";
import  Button  from '@mui/material/Button';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';

import SearchIcon from "@mui/icons-material/Search";
import TextField from "@mui/material/TextField";
import request from "../axio/request";

const Search=()=>{
    const [search,setsearch]=useState(null);
    const [bill,setbill]=useState([]);
    const [billlid,setbillid]=useState(null);
    const [billldoc,setbilldoc]=useState([]);
    const [billlcoll,setbillcol]=useState([]);
    const [billlnote,setbilllnote]=useState(null);
    const searchbil= async (e)=>{
        e.preventDefault();
        try{
            console.log(e)
            console.log(search)
            let bb=await request.getbilid(search);
            console.log(bb['bilid'])
            setbill(bb)
        }catch(e){
            console.error(e);
        }

        // const form = (e,value)=>{
            
        
        // }

        // form()
    }
    useEffect(()=>{
        const bbiill=()=>{
            console.log(bill);
            const {bilid,billdoc,billtime,bilnote,collctionid} = bill;
            console.log(bilid,'billid')
            setbillid(bilid)
            setbillcol(collctionid)
            setbilldoc(billdoc)
            setbilllnote(bilnote)
            console.log(billdoc)
            console.log(billtime)
            console.log(bilnote)
            // console.log(co)
            

        }
        bbiill()
    },[bill])
    console.log(billlcoll)
    console.log(bill)
    console.log(billldoc);
    return(
        <>
        <IconButton>
        </IconButton>
        <form onSubmit={searchbil}>
        <TextField id="search" fullWidth onChange={(e)=>{setsearch(e.target.value)}} placeholder="search bill fro enter billid" label="Searche the bill here" variant="outlined" />
        <center><Button variant="contained" sx={{ m: 1}} type="submit">click to search.. <SearchIcon/></Button></center>

        </form>
    {bill?(<div>
      <h2>Bill Information</h2>
      <p>Bilid: {billlid}</p>
      <p>Billed by Docter:- {billldoc?.username}</p>
   
      <p>Bill Note: {billlnote}</p>
      <ul>
        <h1>medicine for desies</h1>
            <li><h3>Desies :- {billlcoll?.subdesies?.subdesiesna}</h3><FormControlLabel required control={<Checkbox />} label="Cheack in" /></li>
            <li><h3>Medicine :- {billlcoll?.medicine?.medename}</h3><FormControlLabel required control={<Checkbox />} label="Cheack in" /></li>
            <li><h3>Note for Medicine:- {billlcoll?.note}</h3></li>
            <li><h3>Give Mdicine for :- {billlcoll?.days} Days</h3></li>




      </ul>
    </div>):(<h1>search bill id</h1>)}
        </>
        
    )
}
export default Search;