import React, { useState } from "react";
import background from "../../public/background_image.png";
import { Result } from "../../components/result";
import { Forms } from "../../components/forms";
import { Loading } from "../../components/loading";
import axios from "axios";

interface ResultType {
  name: string;
  image: string;
  flower_symbolism: string;
  example: string;
}

export default function Search() {
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [result, setResult] = useState<ResultType | null>(null);

  const handleClick = async (opponent: string, feeling: string) => {
    setIsLoading(true);
    await axios
      .post("https://floral-gifter-q967.onrender.com", {
        content: { opponent: opponent, feeling: feeling },
      })
      .then((res) => {
        setResult(res.data);
        setIsLoading(false);
        console.log(res);
      })
      .catch((err) => {
        setIsLoading(false);
        alert("回答の生成に失敗しました。もう一度お試しください。");
        console.error(err);
      });
  };

  return (
    <>
      {
        <div className="container">
          {!isLoading && !result && <Forms handleClick={handleClick} />}
          {isLoading && <Loading />}
          {result && (
            <Result
              name={result.name}
              image={result.image}
              flower_symbolism={result.flower_symbolism}
              example={result.example}
            />
          )}
        </div>
      }

      <style jsx>{`
        .container {
          width: 100%;
          height: 100vh;
          background-image: url(${background.src});
          background-size: cover;
          overflow: hidden;
          display: flex;
          justify-content: center;
          align-items: center;
        }
      `}</style>
    </>
  );
}
