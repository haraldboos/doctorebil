import { useEffect,useState,useContext } from "react";
import Authuser from "../context/aut";
import SSmms from "./sms";
// import Medicontext from "../axio/medi";
// import PropTypes from 'prop-types';
import Container from '@mui/material/Container';

import Button from '@mui/material/Button';
import FormControl from '@mui/material/FormControl';
import request from '../axio/request'
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';

const Medi = ()=>{
    const { user } = useContext(Authuser); 

    // const {medic} =useContext(Medicontext);
    const [billnum,setbillnum]=useState(null);

    const [medicinee,setmedicine]=useState([]);
    const [desies,setdesies]=useState([]);
    const [maindaarry,setmaindarray]=useState([]);
    const [selectmaindesies,setmaind]=useState(null);
    // value to update in the post
    const [subdesiesid,setSubdesiesid]=useState(null);
    const [note,setnote]=useState(null);
    const [bilnote,setbilnote]=useState(null);

    const [dayss,setDays]=useState(null);
    const [medicine,setMedicine]=useState(null);
    const [medid,setmedid]=useState(null);
    const [mobilenum,setmobilenum]=useState(null);


    const collanbill = (e)=>{
        e.preventDefault();
        // console.log(e,111111111)
        // console.log(subdesiesid)
        const data ={
            "user": user,
            "subdesies_id": subdesiesid,
            "note":note,
            "days":dayss,
            "medicine_id": medid,
            "smsnumber":mobilenum,
            "billnote":bilnote
        }
        const makecoll=async (data)=>{
            try{
                const collpost = await request.colle(data);
                console.log(collpost,1231231231);
                setbillnum(collpost['bilid']);
            }catch(e){
                console.error(e)
            }

        }
        makecoll(data);
    }
    // const handelfuck =(event,v)=>{
    //     event.preventDefault();
    //     setmaind(v);
    //     console.log(v,selectmaindesies);
        

    // }
    // console.log(selectmaindesies);

    useEffect(()=>{
        const getdata = async()=>{
            try{
                const reasult = await request.medic();
                let {medicine,desies}=reasult;
                setmedicine(medicine)
                setdesies(desies);
                // console.log(reasult);
                // console.log(medicine);
                
            }catch(error){
                console.error('error fetch data',error);
            }
        }
        getdata()
    },[]);
    useEffect(()=>{
        if(desies){
            const maindset = new Set();
            desies.forEach(des=>maindset.add(des.maindesis.desiesname));
            const maind=Array.from(maindset);
            setmaindarray(maind);
            // console.log(maind,1)
        }
    },[desies]);
    // console.log(desies);
    // console.log(subdesiesid)
    // console.log(note)
    // console.log(dayss)

    return (
        <>
        <Container fixed>
        <form onSubmit={collanbill}>
        <FormControl sx={{ m: 1, width: '25ch' }} variant="outlined">
        {/* <Container fixed sx={{ border: "1px solid red"}}> */}

        <Autocomplete
      disablePortal
      id="Main_desies"
      options={maindaarry.map((it)=>it)}
      sx={{ width: 300,m:2 }}
      onChange={(event,value)=>setmaind(value)}
      renderInput={(params) => <TextField {...params} label="Main desies" />}
    />
    {selectmaindesies&&(<Autocomplete
        disablePortal
        id="Sub_desies"
        options={desies.filter((item)=>item.maindesis.desiesname ===selectmaindesies).map(it=>it.subdesiesna)}
        sx={{ width: 300,m:2 }}
        // onChange={(event, value) => setSubdesiesid(value.minidid)}
        onChange={(event, value) =>{
            console.log(typeof(value))
                // setSubdesiesid(value&&{desies.find(oo=>oo.subdesiesna===value)})
            if(value){
                let selectobj=desies.find(oo=>oo.subdesiesna===value)
                setSubdesiesid(selectobj.minidid)
            }        
                
        
        }}

        renderInput={(params) => <TextField {...params} label="Subdesies" />}
      />)}
        <Autocomplete
      disablePortal
      id="Medicine"
      options={medicinee.map(it=>it.medename)}
      sx={{ width: 300,m:2 }}
      onChange={(eve,valu)=>{
        setMedicine(valu)
        if(valu){
            let medobj = medicinee.find(pp=>pp.medename===valu)
            setmedid(medobj.medineid)
            
        }
    }

    }
      renderInput={(params) => <TextField {...params} label="Medicine" />}
      
    />
    <TextField id="Days" label="Days" type="number" onChange={(eve)=>setDays(eve.target.value)}InputLabelProps={{shrink: true,}}sx={{ width: 300,m:2 }} variant="outlined"/>

    <TextField id="note" fullWidth sx={{ width: 300,m:2 }} label="enternote" onChange={(eve)=>setnote(eve.target.value)} variant="outlined" />
    {/* </Container> */}
    <TextField id="mobilenumber" fullWidth sx={{ width: 300,m:2 }} label="entermobilenumber" onChange={(eve)=>setmobilenum(eve.target.value)} variant="outlined" />
    <TextField id="bill note" fullWidth sx={{ width: 300,m:2 }} label="give a bill note "  rows={4}  onChange={(eve)=>setbilnote(eve.target.value)} variant="outlined" />
        {/* <input type="number" name="days" onChange={(eve)=>setDays(eve.target.value)}/> */}
       


        {/* <h1>{medicinee.map((i,k)=>(<h2 key={k}>{i.medename}</h2>))}</h1> */}
        <Button variant="contained"type="submit" sx={{ width: 300,m:2 }} >click to create bill</Button>
        </FormControl>
        </form>
        </Container>
        {/* <Container fixed>  */}
        <h1>{subdesiesid}</h1>
        <h1>{note}</h1>
        <h1>{dayss}</h1>
        <h1>{medicine}</h1>
        <h1>{medid}</h1>
        <h1>{mobilenum}</h1>
        <h1>{bilnote}</h1>

        {billnum?<h1>ur bill id is here it wiil send in sms<SSmms message={`this is ur id for mdeical bill show it in near pharmacy ${billnum}`} smsnumber={parseInt(mobilenum)}/> {billnum}</h1>:<h1>nonobill generated</h1>}
{/* </Container> */}
        </>
        
    )
     
    
}

// Medi.propTypes={
//     children:PropTypes.node.isRequired
// };
 /* {medicine ? (<ul>{medicine.map(i=>(<li key={i.key}>{i}</li>))}</ul>):<h2>Nothing is founded</h2>} */
export default Medi;