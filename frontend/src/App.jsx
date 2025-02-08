import { Container, HStack } from "@chakra-ui/react";
import { Navbar } from "./components/Navbar";

function App() {
  return (
    <HStack minH={"100vh"} align={"stretch"} >
      <Navbar />

      <Container maxW={"1200px"} my={4}>
        
      </Container>
    </HStack>
  );
}

export default App;