// Firebase setup
import firebase from 'firebase/app';
import 'firebase/auth';
import 'firebase/firestore';
import 'firebase/storage';

const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  // Add other Firebase config properties
};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const firestore = firebase.firestore();
const storage = firebase.storage();

// User Authentication
const signUp = (email, password) => {
  return auth.createUserWithEmailAndPassword(email, password);
};

const signIn = (email, password) => {
  return auth.signInWithEmailAndPassword(email, password);
};

const signOut = () => {
  return auth.signOut();
};

// Firestore Database
const createRoom = (name, topic) => {
  return firestore.collection('rooms').add({
    name,
    topic,
    createdAt: firebase.firestore.FieldValue.serverTimestamp(),
  });
};

const getAllRooms = () => {
  return firestore.collection('rooms').get();
};

const addMessageToRoom = (roomId, message) => {
  return firestore.collection('rooms').doc(roomId).collection('messages').add({
    text: message,
    timestamp: firebase.firestore.FieldValue.serverTimestamp(),
  });
};

// Real-time Messaging
const listenForMessages = (roomId, callback) => {
  firestore.collection('rooms').doc(roomId).collection('messages')
    .orderBy('timestamp')
    .onSnapshot((snapshot) => {
      snapshot.docChanges().forEach((change) => {
        if (change.type === 'added') {
          const message = change.doc.data();
          callback(message);
        }
      });
    });
};

// File Uploads
const uploadFile = (file) => {
  const storageRef = storage.ref();
  const fileRef = storageRef.child(file.name);
  return fileRef.put(file);
};

const getFileDownloadURL = (fileName) => {
  const fileRef = storage.ref().child(fileName);
  return fileRef.getDownloadURL();
};

// Reactions
const addReactionToMessage = (roomId, messageId, reaction) => {
  return firestore.collection('rooms').doc(roomId)
    .collection('messages').doc(messageId)
    .collection('reactions').add({
      reaction,
      timestamp: firebase.firestore.FieldValue.serverTimestamp(),
    });
};

const getReactionsForMessage = (roomId, messageId) => {
  return firestore.collection('rooms').doc(roomId)
    .collection('messages').doc(messageId)
    .collection('reactions').get();
};
