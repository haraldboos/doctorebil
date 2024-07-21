// import { ACCESS_TOKEN,REFRESH_TOKEN } from "./constants";
// import opai from  "../api";
// import { useState,useEffect } from "react";
// import {Navigate} from "react-router-dom"
// import {jwtDecode} from "jwt-decode"
// function Securerouting(children){
//     const [isauth,setisauth]=useState(null)
//     useEffect(()=>{
//         autconst().catch(()=>setisauth(false));
//     },[]);
//     const refreshtok = async ()=>{
// // wait for code
//         const retk = localStorage.getItem(REFRESH_TOKEN)
//         try{
//             const res = await opai.post("/token/refresh/",{
//                 refresh:retk,

//             });
//             if (res.status === 200){
//                 localStorage.setItem(ACCESS_TOKEN,res.data.access)
//                 setisauth(true)
//             }else{
//                 setisauth(false)
//             }
//         }catch (e){
//             console.log(e)
//             setisauth(false);
//         }
//     }
//     const autconst = async()=>{
//         // auth
//         const token =localStorage.getItem(ACCESS_TOKEN)
//         if (!token){
//             setisauth(false)
//             return
//         }
//             const dcd = jwtDecode(token)
//             console.log(dcd)
//             const tkenexp = dcd.exp
//             const now = Date.now()/1000

//             if (tkenexp<now){
//                 await refreshtok()

//             }else{
//                 setisauth(true)
//             }
//     }
//     if (isauth === null){
//         return <div><h1>LOADING....</h1></div>
//     }
//     return isauth ? children : <Navigate to="/login" />;

// }
// export default Securerouting