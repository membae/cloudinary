import React, { useState } from "react";
import Axios from "axios";
import {Image} from "cloudinary-react"

function Upload() {
  const [imageSelected, setImageSelected] = useState();
  const [uploadedImageUrl,setUploadedImageUrl]=useState("")

  const uploadImage = () => {
    // console.log(files[0])
    const formData = new FormData();
    formData.append("file", imageSelected);
    formData.append("upload_preset", "azoncode");

    Axios.post(
      "https://api.cloudinary.com/v1_1/dia2le5vz/image/upload",
      formData
    ).then((res) => {
      console.log(res);
      setUploadedImageUrl(res.data.secure_url)
    });
  };

  return (
    <div>
      <div>
        <h1>A button to upload images</h1>
      </div>
      <div>
        <input
          type="file"
          onChange={(event) => {
            setImageSelected(event.target.files[0]);
          }}
        />
        <button onClick={uploadImage}> Upload image</button>
        <Image cloudName="dia2le5vz" publicId={uploadedImageUrl}/>
      </div>
    </div>
  );
}

export default Upload;
