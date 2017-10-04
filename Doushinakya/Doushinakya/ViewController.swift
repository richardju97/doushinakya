//
//  ViewController.swift
//  Doushinakya
//
//  Created by Richard Ju on 9/30/17.
//  Copyright © 2017 Richard Ju. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }

    @IBOutlet weak var VerbDic: NSTextField!
    @IBOutlet weak var DispVerb: NSTextField!
    
    @IBAction func Submit(_ sender: NSButton) {
        let url = URL(string: "http://jisho.org/api/v1/search/words?keyword=食べる")

//        let task = URLSession.shared.dataTask(with: url! as URL) { data, response, error in
//
//            guard let data = data, error == nil else { return }
//            print(NSString(data: data, encoding: String.Encoding.utf8.rawValue))
//        }
//        
//        task.resume()
        
        let doushi = VerbDic.stringValue
        
        DispVerb.stringValue = doushi
    }
}

