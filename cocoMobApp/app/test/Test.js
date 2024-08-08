
import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import axios from 'axios';

const App = () => {
  const [nom, setNom] = useState('');
  const [email, setEmail] = useState('');
  const [motDePasse, setMotDePasse] = useState('');

  const handleInscription = () => {
    axios.post('http://localhost:8000/inscription/', {
      nom,
      email,    
      mot_de_passe: motDePasse,
    })
      .then(response => console.log(response.data))
      .catch(error => console.error(error));
  };

  return (
    <View>
      <Text>Inscription</Text>
      <TextInput
        placeholder="Nom"
        value={nom}
        onChangeText={setNom}
      />
      <TextInput
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
      />
      <TextInput
        placeholder="Mot de passe"
        secureTextEntry
        value={motDePasse}
        onChangeText={setMotDePasse}
      />
      <Button title="S'inscrire" onPress={handleInscription} />
    </View>
  );
};

export default App;