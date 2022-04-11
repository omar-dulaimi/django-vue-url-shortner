export const isValidHttpUrl = (string) => {
  let urlToTest;
  try {
    urlToTest = new URL(string);
  } catch (_) {
    return false;
  }

  return urlToTest.protocol === "http:" || urlToTest.protocol === "https:";
};
