package main

import "fmt"

// YouTuber interface with method signatures
type YouTuber interface {
    CreateContent() string
    GetSubscriberCount() int
}

type ComputerScienceYoutuber struct {
    Name        string
    Subscribers int
    VideoTopics []string
}

func (csy ComputerScienceYoutuber) CreateContent() string {
    return fmt.Sprintf("Coding tutorial on %s", csy.VideoTopics[0])
}

func (csy ComputerScienceYoutuber) GetSubscriberCount() int {
    return csy.Subscribers
}

type MusicYoutuber struct {
    Name        string
    Subscribers int
    Genre       string
}

func (my MusicYoutuber) CreateContent() string {
    return fmt.Sprintf("Music video in %s genre", my.Genre)
}

func (my MusicYoutuber) GetSubscriberCount() int {
    return my.Subscribers
}

// AnalyzeYouTuber takes any type that implements the YouTuber interface
func AnalyzeYouTuber(y YouTuber) {
    fmt.Printf("Content Created: %s\n", y.CreateContent())
    fmt.Printf("Subscriber Count: %d\n", y.GetSubscriberCount())
}

func main() {
    techYoutuber := ComputerScienceYoutuber{
        Name:        "Prof Korupt",
        Subscribers: 4150,
        VideoTopics: []string{"Go Interface"},
    }
    
    var my YouTuber
    my = MusicYoutuber{
        Name:        "KoruptChords",
        Subscribers: 50,
        Genre:       "Classical",
    }
    fmt.Println(my.GetSubscriberCount())
    AnalyzeYouTuber(techYoutuber)

}