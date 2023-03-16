import { useState } from "react";
import axios from "axios";
import { MdFileUpload } from "react-icons/md";
interface BirdData {
  species: string;
  predicted_class_label: string;
  origin: string;
  description: string;
}

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [data, setData] = useState<BirdData | null>(null);
  return (
    <div className="flex items-center flex-col justify-center h-screen px-40 customBG relative bg-black/30">
      {loading && (
        <div className="absolute top-0 left-0 w-full h-full bg-black/50 flex items-center justify-center">
          <div className="lds-ring">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
          </div>
        </div>
      )}
      <h1 className="text-5xl font-bold pb-10 text-white capitalize">
        Identification on bird species using audio signal processing
      </h1>
      <div className="">
        {data && (
          <div className="flex-col flex items-center">
            <img
              src={data.species + ".jpg"}
              alt="bird"
              className="w-80 h-80 rounded-full object-cover"
            />
            <h1 className="text-5xl py-5 font-bold">{data.species}</h1>
            <table>
              {Object.entries(data).map(([key, value]) => (
                <tr key={key}>
                  <td className="capitalize font-bold">
                    {key.replace("_", " ")}
                  </td>
                  <td>{value}</td>
                </tr>
              ))}
            </table>
          </div>
        )}
      </div>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          setLoading(true);
          if (file) {
            axios
              .post(
                "http://localhost:5000/getSong",
                { file: file },
                {
                  headers: {
                    "Content-Type": "multipart/form-data",
                  },
                }
              )
              .then((res) => {
                setData(res.data as BirdData);
                setLoading(false);
              });
          }
        }}
        className="flex flex-col"
      >
        <label
          htmlFor="file"
          className="border bg-white  text-blue-500 border-blue-500 rounded-md px-8 flex flex-row justify-evenly items-center gap-x-4 "
        >
          <h3 className="text-2xl font-bold">Upload Audio File</h3>
          <MdFileUpload className="text-5xl" />
          <input
            type="file"
            id="file"
            accept="audio/*"
            name="file"
            className="hidden"
            onChange={(e) => {
              setFile(e.target.files?.item(0) ?? null);
            }}
          />
        </label>
        <button
          className="px-4 py-2 font-bold text-2xl uppercase bg-blue-500 text-white rounded-md"
          type="submit"
        >
          Submit
        </button>
      </form>
    </div>
  );
}

export default App;
