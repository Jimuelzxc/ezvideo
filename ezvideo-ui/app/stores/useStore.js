import { create } from 'zustand'

const useStore = create((set) => ({
  data: {
    title:"",
    script:"",
  },
}))
