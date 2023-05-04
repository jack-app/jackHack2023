import React from "react";

interface ResultProps {
  result: {
    name: string;
    image: string;
    flower_symbolism: string;
    example: string;
  };
}

export const Result: React.FC<ResultProps> = (result) => {
  return (
    <>
      <div>結果です</div>
      <style jsx>{``}</style>
    </>
  );
};
