import { kea } from 'kea'
import { counterLogicType } from './counterLogicType'

export const counterLogic = kea<counterLogicType>({
    actions: {
        incrementCounter: true, // https://kea.js.org/docs/guide/concepts#actions
        decrementCounter: true, // true является сокращением для функции, которая не получает аргументов
        updateCounter: (newValue: number) => ({ newValue }),
    },
    reducers: {
        count: [
            0, // значение по умолчанию
            {
                incrementCounter: (state) => state + 1,
                decrementCounter: (state) => state - 1,
                updateCounter: (_, { newValue }) => newValue, // игнорировать состояние, установить новое значение
            },
        ],
    },
})